from pandas import DataFrame
import streamlit as st

# st.markdown("<h1 style='text-align: center; color: black;'>KAPI</h1>", unsafe_allow_html=True)

st.title('KAPI')
st.markdown('''Welcome to a prototype of our Keyboardless, ASL-inspired Programming Interface (**KAPI**)! The purpose of KAPI is to translate sign language 
into Python code, specifically for Machine Learning applications. We aim to remove the need for keyboards
and allow users to freely program using only webcam. The process of our prototype can be broken into gesture recognition, data storage, and code generation.''')

st.image(image='Kapi_arch.png', width=500, caption='KAPI Architecture')

st.subheader('Gesture Recognition')
st.markdown('''For this prototype we relied on Google's [Shuwa Gesture Toolkit](https://github.com/google/shuwa) to process
a person's pose, face, and hand gestures and recognize them as commonly used ML functions. As a preliminary
step, we created and included the following gestures into Shuwa's dataset: 
''')

ml_gestures = DataFrame({'ML Gestures': ['load'] + ['normalize'] + ['reshape'] + ['compile'] + ['evaluate'] + ['render']})
st.table(ml_gestures)

st.subheader('Data Storage')
st.markdown('''Ideally after recognizing the gesture, we would post the classification to our Azure SQL Database. From there, we map the gesture with a 
table that contains the code translations and post that into this website! This helps as we consider the scalability of our app across many users.
_Note that this prototype does not communicate with the database yet, but the tables are created as shown below._''')

st.image(image='Kapi_database.png', width=500, caption='Gesture to Code Translations')

st.image(image='Kapi_user_motions.png', width=500, caption='User data')

st.subheader('Code Generation')
st.markdown('''The table mentioned above was created with the help of [Github Copilot](https://copilot.github.com/). We originally wanted to use 
the full intellisense feature into KAPI, but we could not find a way to call the autocomplete function in Visual Studio (VS) Code without 
pressing `Tab` or `Enter`. Unfortunately without having access to the Copilot code nor having a "hacky" method to call the autocomplete function in VS Code without a 
keyboard, we decided to create our own dataset based on Copilot offline. Alas, this limits the available code translations.''')

st.subheader('Room for Improvement')
st.markdown('''In the future, we'd like the full application to be processed on Azure ML. This would remove the need of opening Shuwa, storing values on a SQL database 
and displaying it on a website. Users may experience some disconnect since they use separate interfaces, and this should be addressed in the future.
For this prototype, we wanted to see how complimentary Shuwa's algorithm would be for our use case, which is real time processing and
code generation (and it seems to do well)! Another constrain is the fact that we do not have full utility with Copilot. Either we devise a hacky way to generate autocomplete or continue
to expand our manually created dataset. Lastly, we were not able to connect to our SQL server at the last minute, so the demo shows code translations, 
if the user gestured the commands for `load`, `normalize`, `compile`, `evaluate`, and `render`.''')

st.subheader('Try it out')
st.markdown('''In another terminal, go to the directory which contains
`webcam_demo_knn.py` and run `python webcam_demo_knn.py` Go to playmode and record your gestures one at a time.

Afterwards click the `Generate Code` button and see what code KAPI generates for you!''') 
gesture, code_translation = [], []


def get_data(table, db, gesture, code_translation):
# # retrieve data from SQL database   
#     query = 'SELECT * FROM {}'.format(table)
#     df = db.query(query)
#     return df

#''' SQL not working at the monent, so we use a hardcoded dataframe '''
    gesture = ['load','normalize', 'compile','evaluate','render']
    code_translation = ['(train_images, train_labels), (test_images, test_labels) = mnist.load_data()',
        '''train_images = train_images / 255.0 \ntest_images = test_images / 255.0''',
        '''model = keras.Sequential([\n '''+
        '''keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),\n keras.layers.MaxPooling2D(2, 2), # pooling layer\n''' + 
        '''keras.layers.Flatten(),\n keras.layers.Dense(128, activation='relu'),\n keras.layers.Dense(10, activation='softmax')\n ])''',
        '''model.compile(optimizer=adam, \nloss=sparse_categorical_crossentropy,\nmetrics=[accuracy])''',
        '''model.summary()''',]
    return gesture, code_translation



with st.form('editor'):
    gen_button = st.form_submit_button(label='Generate Code')
    if gen_button:
        with st.spinner():
            gesture, code_translation = get_data('ml_gestures', 'ml_gestures', gesture, code_translation)
    for ges, code in zip(gesture, code_translation):
        with st.expander(ges):
            st.code(code)
    reset_button = st.form_submit_button(label='Reset')
    if reset_button:
        gesture, code_translation = [], []

_left, mid, _right = st.columns(3)
with mid:
    st.image(image='KAPI_logo.png',caption='KAPI logo.\n(Kapi means monkey in sanskrit)')
