from flask import Flask 
from flask_pymongo import PyMongo , ObjectId
from flask_cors import CORS
from plots import connectToDB
from plots import plot_histogram , plot_boxplot ,plot_scatter ,plot_pie_chart ,plot_line , lr1 , lr2 ,lr3 , kmeans1 , kmeans2
from plots import gmm1 , gmm2 , cor1
app = Flask(__name__)
CORS(app)
app.config['MONGO_URI']='mongodb://localhost/NITIAYOG'
mongo = PyMongo(app)

db = mongo.db.users

@app.route("/")
def index():
    return '<h1>Hello World</h1>'

connectToDB()
# load_db()

@app.route('/hist1', methods=['GET'])
def get_plot_1():
    img_base64 = plot_histogram("Stunted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/hist2', methods=['GET'])
def get_plot_2():
    img_base64 = plot_histogram("Wasted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/hist3', methods=['GET'])
def get_plot_3():
    img_base64 = plot_histogram("Underweight children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/hist4', methods=['GET'])
def get_plot_4():
    img_base64 = plot_histogram("Children age group of 6 to 59 months with Mid-Upper Arm Circumference ( MUAC ) less than 125 cm (%)")
    return {'plot': img_base64}

@app.route('/hist5', methods=['GET'])
def get_plot_5():
    img_base64 = plot_histogram("Children under the age group of 5 years with triceps skinfold (%) less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/hist6', methods=['GET'])
def get_plot_6():
    img_base64 = plot_histogram("Children age group of 1 to 4 years with subscapular skinfold less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/hist7', methods=['GET'])
def get_plot_7():
    img_base64 = plot_histogram("Stunned children age group of 5 to 9 years (%)")
    return {'plot': img_base64}

@app.route('/hist8', methods=['GET'])
def get_plot_8():
    img_base64 = plot_histogram("Overweight or obese children age group of 5-9 years greater than +1 SD (%)")
    return {'plot': img_base64}

@app.route('/hist9', methods=['GET'])
def get_plot_9():
    img_base64 = plot_histogram("Moderate or severely thin adolescents age group of 10 to 14 years less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/hist10', methods=['GET'])
def get_plot_10():
    img_base64 = plot_histogram("Overweight or obese children age group of 5-9 years greater than +1 SD (%)")
    return {'plot': img_base64}

# Box plots 

@app.route('/box1', methods=['GET'])
def get_plot_1b():
    img_base64 = plot_boxplot("Stunted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/box2', methods=['GET'])
def get_plot_2b():
    img_base64 = plot_boxplot("Wasted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/box3', methods=['GET'])
def get_plot_3b():
    img_base64 = plot_boxplot("Underweight children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/box4', methods=['GET'])
def get_plot_4b():
    img_base64 = plot_boxplot("Children age group of 6 to 59 months with Mid-Upper Arm Circumference ( MUAC ) less than 125 cm (%)")
    return {'plot': img_base64}

@app.route('/box5', methods=['GET'])
def get_plot_5b():
    img_base64 = plot_boxplot("Children under the age group of 5 years with triceps skinfold (%) less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/box6', methods=['GET'])
def get_plot_6b():
    img_base64 = plot_boxplot("Children age group of 1 to 4 years with subscapular skinfold less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/box7', methods=['GET'])
def get_plot_7b():
    img_base64 = plot_boxplot("Stunned children age group of 5 to 9 years (%)")
    return {'plot': img_base64}

@app.route('/box8', methods=['GET'])
def get_plot_8b():
    img_base64 = plot_boxplot("Overweight or obese children age group of 5-9 years greater than +1 SD (%)")
    return {'plot': img_base64}

@app.route('/box9', methods=['GET'])
def get_plot_9b():
    img_base64 = plot_boxplot("Moderate or severely thin adolescents age group of 10 to 14 years less than -2 SD (%)")
    return {'plot': img_base64}

@app.route('/box10', methods=['GET'])
def get_plot_10b():
    img_base64 = plot_boxplot("Overweight or obese children age group of 5-9 years greater than +1 SD (%)")
    return {'plot': img_base64}

# Scatter plot

@app.route('/scatter1', methods=['GET'])
def get_plot_1s():
    img_base64 = plot_scatter("Stunted children under the age of 5 years (%)","Severely stunted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/scatter2', methods=['GET'])
def get_plot_2s():
    img_base64 = plot_scatter("Wasted children under the age of 5 years (%)" ,"Severely wasted children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/scatter3', methods=['GET'])
def get_plot_3s():
    img_base64 = plot_scatter("Underweight children under the age of 5 years (%)" ,"Severely underweight children under the age of 5 years (%)")
    return {'plot': img_base64}

@app.route('/scatter4', methods=['GET'])
def get_plot_4s():
    img_base64 = plot_scatter("Stunned children age group of 5 to 9 years (%)" ,"Severely stunted children age group of 5 to 9 years (%)")
    return {'plot': img_base64}

@app.route('/scatter5', methods=['GET'])
def get_plot_5s():
    img_base64 = plot_scatter("Stunned children age group of 5 to 9 years (%)" ,"Severely stunted children age group of 5 to 9 years (%)")
    return {'plot': img_base64}

# Pi charts
@app.route('/piplot1', methods=['GET'])
def get_plot_1p():
    img_base64 = plot_pie_chart( 'Stunted children under the age of 5 years (%)' , 'Residence type')
    return {'plot': img_base64}

@app.route('/piplot2', methods=['GET'])
def get_plot_2p():
    img_base64 = plot_pie_chart('Underweight children under the age of 5 years (%)','State')
    return {'plot': img_base64}

@app.route('/piplot3', methods=['GET'])
def get_plot_3p():
    img_base64 = plot_pie_chart('Wasted children under the age of 5 years (%)', 'Residence type')
    return {'plot': img_base64}

@app.route('/piplot4', methods=['GET'])
def get_plot_4p():
    img_base64 = plot_pie_chart('Severely stunted children under the age of 5 years (%)','Residence type')
    return {'plot': img_base64}

@app.route('/piplot5', methods=['GET'])
def get_plot_5p():
    img_base64 = plot_pie_chart('Wasted children under the age of 5 years (%)', 'State')
    return {'plot': img_base64}

@app.route('/piplot6', methods=['GET'])
def get_plot_6p():
    img_base64 = plot_pie_chart('Children age group of 6 to 59 months with Mid-Upper Arm Circumference ( MUAC ) less than -3 SD (%)', 'State')
    return {'plot': img_base64}

# Line plot
@app.route('/lineplot1', methods=['GET'])
def get_plot_1l():
    img_base64 = plot_line('Year','Stunted children under the age of 5 years (%)')
    return {'plot': img_base64}

@app.route('/lineplot2', methods=['GET'])
def get_plot_2l():
    img_base64 = plot_line('Year','Severely stunted children under the age of 5 years (%)')
    return {'plot': img_base64}

@app.route('/lr1', methods=['GET'])
def apply_lr1():
    img_base64 = lr1()
    return {'plot': img_base64}

@app.route('/lr2', methods=['GET'])
def apply_lr2():
    img_base64 = lr2()
    return {'plot': img_base64}

@app.route('/lr3', methods=['GET'])
def apply_lr3():
    img_base64 = lr3()
    return {'plot': img_base64}

@app.route('/kmeans1', methods=['GET'])
def apply_kmean1():
    img_base64 = kmeans1()
    return {'plot': img_base64}

@app.route('/kmeans2', methods=['GET'])
def apply_kmean2():
    img_base64 = kmeans2()
    return {'plot': img_base64}

@app.route('/gmm1', methods=['GET'])
def apply_gmm1():
    img_base64 = gmm1()
    return {'plot': img_base64}

@app.route('/gmm2', methods=['GET'])
def apply_gmm2():
    img_base64 = gmm2()
    return {'plot': img_base64}

@app.route('/cor1', methods=['GET'])
def apply_cor1():
    img_base64 = cor1()
    return {'plot': img_base64}

if __name__ == '__main__':
    app.run(debug=True)