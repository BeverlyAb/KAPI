from pandas import DataFrame
import streamlit as st
import os


st.subheader('Try it out')
st.markdown('''In another terminal, go to the directory which contains
`webcam_demo_knn.py` and run `python webcam_demo_knn.py` Go to playmode and record your gestures one at a time.

Afterwards click the `Generate Code` button and see what code KAPI generates for you!''') 
gesture, code_translation = [], []

# get current directory
path = os.getcwd()
# path = os.path.dirname()

def get_data(file_name):
    gesture_library = ['ASL_load','ASL_normalize', 'ASL_compile','ASL_evaluate','ASL_render']
    code_translation = ['(train_images, train_labels), (test_images, test_labels) = mnist.load_data()',
        '''train_images = train_images / 255.0 \ntest_images = test_images / 255.0''',
        '''model = keras.Sequential([\n '''+
        '''keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),\n keras.layers.MaxPooling2D(2, 2), # pooling layer\n''' + 
        '''keras.layers.Flatten(),\n keras.layers.Dense(128, activation='relu'),\n keras.layers.Dense(10, activation='softmax')\n ])''',
        '''model.compile(optimizer=adam, \nloss=sparse_categorical_crossentropy,\nmetrics=[accuracy])''',
        '''model.summary()''',]
    gesture_code_dict = dict(zip(gesture_library, code_translation))
    # read contents from file
    user_gesture = []
    with open(path+file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() in gesture_library:
                user_gesture.append(line.strip())
    
    sign_code = []
    for ug in user_gesture:
        sign_code.append(gesture_code_dict[ug])
    return user_gesture, sign_code


with st.form('editor'):
    gen_button = st.form_submit_button(label='Generate Code')
    if gen_button:
        with st.spinner():
            gesture, code_translation = get_data('/../shuwa-main/shuwa-main/result.txt')
    for ges, code in zip(gesture, code_translation):
        with st.expander(ges):
            st.code(code)
    reset_button = st.form_submit_button(label='Reset')
    if reset_button:
        gesture, code_translation = [], []
        with open(path+'/../shuwa-main/shuwa-main/result.txt', 'w') as f:
            f.write('')
