from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('doctorrf_fees.pkl','rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        # Profile
        Profile = request.form["Profile"]
        if (Profile == "Ayurveda"):
            Profile_Ayurveda = 1
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0

        elif (Profile == "Dentist"):
            Profile_Ayurveda = 0
            Profile_Dentist = 1
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0

        elif (Profile == "Dermatologists"):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 1
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0

        elif (Profile == "ENT Specialist"):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 1
            Profile_General_Medicine = 0
            Profile_Homeopath = 0

        elif (Profile == "General Medicine"):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 1
            Profile_Homeopath = 0

        elif (Profile == "Homeopath"):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 1

        else:
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0

        # Qualification
        Qualification = request.form["Qualification"]
        if (Qualification == "MBBS"):
            MBBS = 1
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "BDS"):
            MBBS = 0
            BDS = 1
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "BAMS"):
            MBBS = 0
            BDS = 0
            BAMS = 1
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "BHMS"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 1
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "MD Dermatology"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 1
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "MS ENT"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 1
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "Venereology and Leprosy"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 1
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "MD General Medicine"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 1
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        elif (Qualification == "Diploma in Otorhinolaryngology"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 1
            MD_Homeopathy = 0

        elif (Qualification == "MD Homeopathy"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 1

        else:
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0

        # Experience
        Experience = request.form["Experience"]
        Experience = int(Experience)

        # Rating
        Rating = request.form["Rating"]
        Rating = int(Rating)
        if (Rating < 0):
            Rating = 0
        elif (Rating >= 0) & (Rating < 10):
            Rating = 1
        elif (Rating >= 10) & (Rating < 20):
            Rating = 2
        elif (Rating >= 20) & (Rating < 30):
            Rating = 3
        elif (Rating >= 30) & (Rating < 40):
            Rating = 4
        elif (Rating >= 40) & (Rating < 50):
            Rating = 5
        elif (Rating >= 50) & (Rating < 60):
            Rating = 6
        elif (Rating >= 60) & (Rating < 70):
            Rating = 7
        elif (Rating >= 70) & (Rating < 80):
            Rating = 8
        elif (Rating >= 80) & (Rating < 90):
            Rating = 9
        elif (Rating >= 90) & (Rating <= 100):
            Rating = 10
        else:
            Rating = 0

        # city
        city = request.form["city"]
        if (city == "Bangalore"):
            city_Bangalore = 1
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Chennai"):
            city_Bangalore = 0
            city_Chennai = 1
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Coimbatore"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 1
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Delhi"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 1
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Ernakulam"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 1
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Hyderabad"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 1
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Mumbai"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 1
            city_Thiruvananthapuram = 0
            city_Unknown = 0

        elif (city == "Thiruvananthapuram"):
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 1
            city_Unknown = 0

        else:
            city_Bangalore = 0
            city_Chennai = 0
            city_Coimbatore = 0
            city_Delhi = 0
            city_Ernakulam = 0
            city_Hyderabad = 0
            city_Mumbai = 0
            city_Thiruvananthapuram = 0
            city_Unknown = 1

        prediction = model.predict([[
            Experience,
            Rating,
            MBBS,
            BDS,
            BAMS,
            BHMS,
            MD_Dermatology,
            MS_ENT,
            Venereology_Leprosy,
            MD_General_Medicine,
            Diploma_in_Otorhinolaryngology,
            MD_Homeopathy,
            city_Bangalore,
            city_Chennai,
            city_Coimbatore,
            city_Delhi,
            city_Ernakulam,
            city_Hyderabad,
            city_Mumbai,
            city_Thiruvananthapuram,
            city_Unknown,
            Profile_Ayurveda,
            Profile_Dentist,
            Profile_Dermatologists,
            Profile_ENT_Specialist,
            Profile_General_Medicine,
            Profile_Homeopath
        ]])

        Fees = round(prediction[0], 2)

        return render_template('index.html', prediction_text="Your Doctor consultancy Fees is Rs. {}".format(Fees))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
