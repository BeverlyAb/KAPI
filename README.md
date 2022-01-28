# KAPI

## Inspiration
Welcome to a prototype of our Keyboardless, ASL-inspired Programming Interface (KAPI)! The purpose of KAPI is to translate sign language into Python code, specifically for Machine Learning applications. We aim to remove the need for keyboards and allow users to freely program using only webcam. The process of our prototype can be broken into gesture recognition, data storage, and code generation.

## Architecture
<img src='KAPI-website/KAPI_arch.png' title='ERD' width='' alt='arch' />


## Room for Improvement
In the future, we'd like the full application to be processed on Azure ML. This would remove the need of opening Shuwa, storing values on a SQL database and displaying it on a website. Users may experience some disconnect since they use separate interfaces, and this should be addressed in the future. For this prototype, we wanted to see how complimentary Shuwa's algorithm would be for our use case, which is real time processing and code generation (and it seems to do well)! Another constrain is the fact that we do not have full utility with Copilot. Either we devise a hacky way to generate autocomplete or continue to expand our manually created dataset. Lastly, we were not able to connect to our SQL server at the last minute, so the demo shows code translations, if the user gestured the commands for load, normalize, compile, evaluate, and render.

## How to run
In your terminal `pip install -r requirements` Then go to the directory `KAPI-website` and run `streamlit run KAPI-website.py` At the bottom you'll see directions on how to 
run Shuwa. To run the gesture recognition, go to the `shuwa-main` directory that contains `webcam_demo_knn.py` and run `python webcam_demo._knn.py`

## [Prototype Demo](https://uci.zoom.us/rec/share/W0VB84wadmxFiK6sebvmxyJahRw-NFg34JbUCHv-aiaVt3xTf6fqU_5eBeyRpv3k.Rrd6bzJwUMKwo4Cj?startTime=1643409309000)
