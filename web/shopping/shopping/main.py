import os
from flask import *
from forms import *
from sqlalchemy import asc,exc
from models import db

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    if session.get('userid',None) and session.get('point',None) is not None:
        session.pop('userid',None)
        session.pop('point',None)

    login_form = LoginForm()
    try :
        if login_form.validate_on_submit():
            userid = login_form.data.get('userid')
            print('{}가 로그인 했습니다'.format(userid))
            flash('{}님 환영합니다!'.format(userid))
            session['userid'] = userid
            return redirect('/main_page')
    except AttributeError:
        flash("존재하지 않는 아이디입니다!")
        db_session.rollback()
    return render_template('login.html', form=login_form)
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    point = 10000
    if form.validate_on_submit():
        usertable = User()
        usertable.userid = form.data.get('userid')
        usertable.email = form.data.get('email')
        usertable.password = form.data.get('password')
        usertable.point = point
        try:
            db_session.add(usertable)
            db_session.commit()
        except exc.IntegrityError as e:
            flash('아이디 또는 이메일 중복입니다!')
            return redirect('/register')
            db_session.rollback()

        flash('회원가입 성공!')
        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/main_page',methods = ["GET","POST"])
def mainpage():
    userid = session.get('userid',None)
    point = session.get('point',None)
    if userid is None:
        flash("Plz...login..")
        return redirect('/')
    if point is None:
        query = db_session.query(User).filter(User.userid == userid).first()
        point = query.point
    elif point < 0:
        flash("No Hack...")
        point = 0
    session['point'] = point
    return render_template('main_page.html', userid=userid, point=point)

@app.route('/PayProcess',methods=['GET','POST'])
def PayProcess():
    userid = session.get('userid', None)
    if userid is None:
        flash("Plz...login..")
        return redirect('/')
    query = db_session.query(User).filter(User.userid == userid).first()
    if (request.method == 'GET'):
       num = request.args.get('num')

    init_point = session.get('point', None)
    if num == '1':
        if init_point < 2900:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 2900
            flash("구매완료!")
    elif num == '2':
        if init_point < 1400:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 1400
            flash("구매완료!")
    elif num == '3':
        if init_point < 900:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 900
            flash("구매완료!")
    elif num == '4':
        if init_point < 950:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 950
            flash("구매완료!")
    elif num == '5':
        if init_point < 1000:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 1000
            flash("구매완료!")

    elif num == '6':
        if init_point < 9999999:
            flash("포인트가 부족합니다!")
        else:
            init_point -= 9999999
            flash("KCTF{I_CAN_BUY_ANYTHING!}")
    if init_point < 0:
        flash("No hack...")
        return redirect('/logout')
    query.point = init_point
    db_session.commit()
    session['point'] = init_point
    return redirect('/main_page')
@app.route('/logout')
def logout():
    session.pop('userid',None)
    session.pop('point',None)
    return render_template('logout.html')

@app.route('/contact',methods=["GET","POST"])
def contact():
    session_userid = session.get('userid', None)
    if session_userid is None:
        flash("Plz...login..")
        return redirect('/')
    if request.method == "POST":
        userid = request.form.get('userid')
        context = request.form.get('context')
        if not(userid and context):
            flash("둘다 채워주세요!")
            return redirect('/contact')
        else:
            contact = Contact()
            contact.userid = userid
            contact.context = context
            try:
                db_session.add(contact)
                db_session.commit()
                flash('문의 내용이 전송 됬습니다.')
                print("새로운 문의가 올라왔습니다.")
            except:
                db_session.rollback()
                raise
            return redirect('/main_page')
    return render_template('contact.html',userid = session_userid)
@app.route('/admin_page', methods=['GET','POST'])

def admin_page():
    userid = session.get('userid',None)
    if userid is None:
        flash("Plz...login..")
        return redirect('/')
    db = db_session.query(User).filter(User.userid == "5up3rU53r").first()

    form = Admin_RegisterForm()
    if userid == db.userid:
        flash("환영합니다 관리자님")
    else:
        flash("권한이 없습니다!")
        return redirect('/main_page')
    if request.method == "POST":
        usertable = User()
        usertable.userid = form.data.get('userid')
        usertable.email = form.data.get('email')
        usertable.password = form.data.get('password')
        usertable.point = form.data.get('point')
        db_session.add(usertable)
        db_session.commit()
        flash('회원가입 성공!')
        return redirect('/main_page')

    return render_template('admin_page.html',form=form)

@app.route('/board_confirm',methods=['GET','POST'])

def board_confirm():
    userid = session.get('userid',None)
    if userid is None:
        flash("Plz...login..")
        return redirect('/')
    list = Contact.query.order_by(asc(Contact.id))
    return render_template('board_confirm.html', list=list)
@app.route('/board/article/<int:id>/')
def board_contents(id):
    article = Contact.query.get_or_404(id)
    return render_template('board_view.html', article=article)

@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    #데이터베이스---------
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'Shopping.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'CodeByO'

    #db = SQLAlchemy()
    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host="0.0.0.0", port=8000, debug=False)