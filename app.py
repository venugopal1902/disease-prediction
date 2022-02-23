from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
import pandas as pd
import pickle
import numpy as np
with open('disease_prediction.pkl','rb') as f:
    mp  = pickle.load(f)
app = Flask(__name__)

def predict():
   symptoms = ['None','itching', ' skin_rash', ' nodal_skin_eruptions',
       ' dischromic _patches', ' continuous_sneezing', ' shivering',
       ' chills', ' watering_from_eyes', ' stomach_pain', ' acidity',
       ' ulcers_on_tongue', ' vomiting', ' cough', ' chest_pain',
       ' yellowish_skin', ' nausea', ' loss_of_appetite',
       ' abdominal_pain', ' yellowing_of_eyes', ' burning_micturition',
       ' spotting_ urination', ' passage_of_gases', ' internal_itching',
       ' indigestion', ' muscle_wasting', ' patches_in_throat',
       ' high_fever', ' extra_marital_contacts', ' fatigue',
       ' weight_loss', ' restlessness', ' lethargy',
       ' irregular_sugar_level', ' blurred_and_distorted_vision',
       ' obesity', ' excessive_hunger', ' increased_appetite',
       ' polyuria', ' sunken_eyes', ' dehydration', ' diarrhoea',
       ' breathlessness', ' family_history', ' mucoid_sputum',
       ' headache', ' dizziness', ' loss_of_balance',
       ' lack_of_concentration', ' stiff_neck', ' depression',
       ' irritability', ' visual_disturbances', ' back_pain',
       ' weakness_in_limbs', ' neck_pain', ' weakness_of_one_body_side',
       ' altered_sensorium', ' dark_urine', ' sweating', ' muscle_pain',
       ' mild_fever', ' swelled_lymph_nodes', ' malaise',
       ' red_spots_over_body', ' joint_pain', ' pain_behind_the_eyes',
       ' constipation', ' toxic_look_(typhos)', ' belly_pain',
       ' yellow_urine', ' receiving_blood_transfusion',
       ' receiving_unsterile_injections', ' coma', ' stomach_bleeding',
       ' acute_liver_failure', ' swelling_of_stomach',
       ' distention_of_abdomen', ' history_of_alcohol_consumption',
       ' fluid_overload', ' phlegm', ' blood_in_sputum',
       ' throat_irritation', ' redness_of_eyes', ' sinus_pressure',
       ' runny_nose', ' congestion', ' loss_of_smell', ' fast_heart_rate',
       ' rusty_sputum', ' pain_during_bowel_movements',
       ' pain_in_anal_region', ' bloody_stool', ' irritation_in_anus',
       ' cramps', ' bruising', ' swollen_legs', ' swollen_blood_vessels',
       ' prominent_veins_on_calf', ' weight_gain',
       ' cold_hands_and_feets', ' mood_swings', ' puffy_face_and_eyes',
       ' enlarged_thyroid', ' brittle_nails', ' swollen_extremeties',
       ' abnormal_menstruation', ' muscle_weakness', ' anxiety',
       ' slurred_speech', ' palpitations', ' drying_and_tingling_lips',
       ' knee_pain', ' hip_joint_pain', ' swelling_joints',
       ' painful_walking', ' movement_stiffness', ' spinning_movements',
       ' unsteadiness', ' pus_filled_pimples', ' blackheads', ' scurring',
       ' bladder_discomfort', ' foul_smell_of urine',
       ' continuous_feel_of_urine', ' skin_peeling',
       ' silver_like_dusting', ' small_dents_in_nails',
       ' inflammatory_nails', ' blister', ' red_sore_around_nose',
       ' yellow_crust_ooze']
   a = pd.read_csv('symptom_Description.csv')
   b = pd.read_csv('symptom_precaution.csv')
   d  = [ ]
   for i in range(1,18):
      Symptom1 = select('symptom'+str(i),symptoms,name = f's{i}')
      d.append(Symptom1)
   d = input_group('basic info',d)
   d= list(d.values())
   for i in range(len(symptoms)):
       if symptoms[i] in d:
           symptoms[i] = 1
       else: 
           symptoms[i] = 0  
   symptoms = pd.DataFrame(symptoms).T  
  
   
   prediction =  mp.predict(symptoms)
   
   
   
   put_html(f"<h1>{prediction[0]}</h1>")
   
   
   put_column([put_html(f"<h2>Discription of Disease:</h2> "),
               put_html(list(a[a['Disease'] == prediction[0]]['Description'])[0]),
               ])
   
   
   put_html('<h3>Precautions for Disease:</h3>')
   
   put_column([
               put_text('1.'+str( list(b[b['Disease'] == prediction[0]]['Precaution_1'])[0])),
               put_text('2.'+ str(list(b[b['Disease'] == prediction[0]]['Precaution_2'])[0])),
               put_text('3.'+ str(list(b[b['Disease'] == prediction[0]]['Precaution_3'])[0])),
               put_text('4.'+ str(list(b[b['Disease'] == prediction[0]]['Precaution_4'])[0]))])
   
   put_html('<a href="/" style="background-color:blue;margin-left:350px;color:white;;padding :8px;border-radius:5px;font-size:30px;text-decoration:none;box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)">Home</a>')
  
  
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)          
   
  
# if __name__ == '__main__':
#        start_server(predict, port=8000, debug=True)
   
    
       
   
   
     