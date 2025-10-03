from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User, Transaction, Budget, Bill, Tax
from werkzeug.security import check_password_hash, generate_password_hash

def register_routes(app):
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            
            if not name or not email or not password:
                flash('Please fill all fields')
                return redirect(url_for('register'))
            
            if User.query.filter_by(email=email).first():
                flash('Email already registered')
                return redirect(url_for('register'))
            
            user = User(
                name=name,
                email=email,
                password=generate_password_hash(password)
            )
            
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
            
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password')
                
        return render_template('login.html')

    @app.route('/dashboard')
    @login_required
    def dashboard():
        transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).limit(5).all()
        budgets = Budget.query.filter_by(user_id=current_user.id).all()
        bills = Bill.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', transactions=transactions, budgets=budgets, bills=bills)

    @app.route('/transactions')
    @login_required
    def transactions():
        transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).all()
        return render_template('transactions.html', transactions=transactions)

    @app.route('/bills')
    @login_required
    def bills():
        from datetime import datetime
        bills = Bill.query.filter_by(user_id=current_user.id).order_by(Bill.due_date).all()
        return render_template('bills.html', bills=bills, now=datetime.now())

    @app.route('/bills/add', methods=['GET', 'POST'])
    @login_required
    def add_bill():
        if request.method == 'POST':
            name = request.form.get('name')
            amount = request.form.get('amount')
            due_date = request.form.get('due_date')
            
            if not name or not amount or not due_date:
                flash('Please fill all required fields')
                return redirect(url_for('add_bill'))

            try:
                amount = float(amount)
                from datetime import datetime
                due_date = datetime.strptime(due_date, '%Y-%m-%d')
                
                bill = Bill(
                    name=name,
                    amount=amount,
                    due_date=due_date,
                    status='unpaid',
                    user_id=current_user.id
                )
                db.session.add(bill)
                db.session.commit()
                flash('Bill added successfully')
                return redirect(url_for('bills'))
            except (ValueError, TypeError):
                flash('Invalid amount or date format')
                return redirect(url_for('add_bill'))

        return render_template('add_bill.html')

    @app.route('/bills/<int:bill_id>/toggle', methods=['POST'])
    @login_required
    def toggle_bill_status(bill_id):
        bill = Bill.query.get_or_404(bill_id)
        if bill.user_id != current_user.id:
            abort(403)
        
        bill.status = 'paid' if bill.status == 'unpaid' else 'unpaid'
        db.session.commit()
        return redirect(url_for('bills'))

    @app.route('/budgets')
    @login_required
    def budgets():
        from datetime import datetime
        budgets = Budget.query.filter_by(user_id=current_user.id).all()
        return render_template('budgets.html', budgets=budgets, now=datetime.now())

    @app.route('/tax')
    @login_required
    def tax():
        from datetime import datetime
        current_year = datetime.now().year
        tax_records = Tax.query.filter_by(user_id=current_user.id).order_by(Tax.year.desc()).all()
        return render_template('tax.html', tax_records=tax_records, current_year=current_year)

    @app.route('/tax/add', methods=['GET', 'POST'])
    @login_required
    def add_tax():
        if request.method == 'POST':
            year = request.form.get('year')
            income = request.form.get('income')
            tax_paid = request.form.get('tax_paid')
            deductions = request.form.get('deductions')
            
            if not year or not income or not tax_paid:
                flash('Please fill all required fields')
                return redirect(url_for('add_tax'))

            try:
                year = int(year)
                income = float(income)
                tax_paid = float(tax_paid)
                deductions = float(deductions) if deductions else 0.0
                
                # Check if tax record already exists for the year
                existing_tax = Tax.query.filter_by(user_id=current_user.id, year=year).first()
                if existing_tax:
                    flash('Tax record already exists for this year')
                    return redirect(url_for('add_tax'))
                
                tax = Tax(
                    year=year,
                    income=income,
                    tax_paid=tax_paid,
                    deductions=deductions,
                    user_id=current_user.id
                )
                db.session.add(tax)
                db.session.commit()
                flash('Tax record added successfully')
                return redirect(url_for('tax'))
            except (ValueError, TypeError):
                flash('Invalid input values')
                return redirect(url_for('add_tax'))

        return render_template('add_tax.html')

    @app.route('/budgets/add', methods=['GET', 'POST'])
    @login_required
    def add_budget():
        if request.method == 'POST':
            category = request.form.get('category')
            amount = request.form.get('amount')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            
            if not category or not amount or not start_date or not end_date:
                flash('Please fill all required fields')
                return redirect(url_for('add_budget'))

            try:
                amount = float(amount)
                from datetime import datetime
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                
                if end_date <= start_date:
                    flash('End date must be after start date')
                    return redirect(url_for('add_budget'))
                
                budget = Budget(
                    category=category,
                    amount=amount,
                    start_date=start_date,
                    end_date=end_date,
                    user_id=current_user.id
                )
                db.session.add(budget)
                db.session.commit()
                flash('Budget added successfully')
                return redirect(url_for('budgets'))
            except (ValueError, TypeError):
                flash('Invalid amount or date format')
                return redirect(url_for('add_budget'))

        return render_template('add_budget.html')

    @app.route('/transactions/add', methods=['GET', 'POST'])
    @login_required
    def add_transaction():
        if request.method == 'POST':
            amount = request.form.get('amount')
            description = request.form.get('description')
            category = request.form.get('category')
            transaction_type = request.form.get('type')

            if not amount or not description or not category or not transaction_type:
                flash('Please fill all required fields')
                return redirect(url_for('add_transaction'))

            try:
                amount = float(amount)
                transaction = Transaction(
                    amount=amount,
                    description=description,
                    category=category,
                    type=transaction_type,
                    user_id=current_user.id
                )
                db.session.add(transaction)
                db.session.commit()
                flash('Transaction added successfully')
                return redirect(url_for('transactions'))
            except ValueError:
                flash('Invalid amount')
                return redirect(url_for('add_transaction'))

        return render_template('add_transaction.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))