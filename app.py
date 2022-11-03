import streamlit as  st
import pandas as pd
import pickle
import numpy as np
def predict(data):
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
    return model.predict(data)




st.title('Previsor de Energia Eolica - Machine Learning ')
st.write('Um Web app que preve a geração de energia eolica ')


Cosphi_avg=st.number_input('Input the converter torque(NM):')

Ds_avg=st.number_input('Input the generator speed (RPM): ')

Ws1_avg=st.number_input('Input the Wind speed 1 (KM): ')

Ws2_avg=st.number_input('Input the wind speed 2 (KM):')

Ws_avg=st.number_input('Input the wind speed 3 (KM):')

Rs_avg=st.number_input('Input the Rotor speed (RPM):')

Na_c_avg=st.number_input('Input the  Nacele Angle: (RPM)')


if st.button('Predict'):
      result = predict(np.array([[Cosphi_avg,Ds_avg,Ws1_avg,Ws2_avg,Ws_avg,Rs_avg,Na_c_avg]]))
      st.success('A quantidade de energia gerada será : {}  Kwhs'.format(result))
