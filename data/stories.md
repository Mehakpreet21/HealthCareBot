## general_sick_story
* greet
  - utter_greet
* sick
  - utter_im_sorry
  - form_questions
  - form{"name":"form_questions"}
  - form{"name":null}
  - utter_ask_symptoms
* symptoms
  - action_side
* side
  - symptom_search
* intensity
  - action_intensity
* picking_specialty
  - utter_ask_doyouwantappointment
* deny
  - utter_anything_else_icanhelpwith
* deny
  - utter_goodbye


## general_sick_story
  * greet
    - utter_greet
  * sick
    - utter_im_sorry
    - form_questions
    - form{"name":"form_questions"}
    - form{"name":null}
    - utter_ask_symptoms
  * symptoms
    - action_side
  * side
    - symptom_search
  * intensity
    - action_intensity
  * picking_specialty
    - utter_ask_doyouwantappointment
  * deny
    - utter_anything_else_icanhelpwith
  * affirm
    - utter_greet

## general_sick_story
* greet
    - utter_greet
* make_appointment
  - utter_ask_doctor
* doc_name{"doctor": "Dr. Tyagi"}
  - slot{"doctor": "Dr. Tyagi"}
  - utter_ask_symptoms
* symptoms
  - action_side
* side
  - symptom_search
* intensity
  - action_intensity
  - utter_appointment_maker
* pick_time
    - utter_appointment_made

## sick_with_side
* symptoms{"symptom": "ear pain"}
    - slot{"symptom": "ear pain"}
    - action_side
* side
    - symptom_search
* intensity
    - action_intensity
* picking_specialty
    - utter_ask_doyouwantappointment
* deny
    - utter_anything_else_icanhelpwith
* affirm
    - utter_greet
## sick_with_side
    * symptoms{"symptom": "ear pain"}
        - slot{"symptom": "ear pain"}
        - action_side
    * side
        - symptom_search
    * intensity
        - action_intensity
    * picking_specialty
        - utter_ask_doyouwantappointment
    * affirm
        - utter_ask_location
    * location_entry
        - utter_ask_doctor
    * doc_name
        - utter_appointment_maker
    * pick_time
        - utter_appointment_made
        - summarize
        - utter_anything_else_icanhelpwith
    * affirm
        - utter_greet
## sick_with_side
* symptoms{"symptom": "ear pain"}
      - slot{"symptom": "ear pain"}
      - action_side
* side
      - symptom_search
* intensity
      - action_intensity
* picking_specialty
      - utter_ask_doyouwantappointment
* affirm
      - utter_ask_location
* location_entry
      - utter_ask_doctor
* doc_name
      - utter_appointment_maker
* pick_time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith
* affirm
      - utter_greet

## sick_with_side
      * symptoms{"symptom": "ear pain"}
            - slot{"symptom": "ear pain"}
            - action_side
      * side
            - symptom_search
      * intensity
            - action_intensity
      * picking_specialty
            - utter_ask_doyouwantappointment
      * affirm
            - utter_ask_location
      * location_entry
            - utter_ask_doctor
      * doc_name
            - utter_appointment_maker
      * pick_time
            - utter_appointment_made
            - summarize
            - utter_anything_else_icanhelpwith
      * deny
            - utter_goodbye

## interactive_story_2
* greet
  - utter_greet
* sick
  - utter_im_sorry
  - form_questions
  - form{"name":"form_questions"}
  - form{"name":null}
  - utter_ask_symptoms
* symptoms{"symptom": "leg pain"}
    - slot{"symptom": "leg pain"}
    - action_side
* side{"side": "left"}
    - slot{"side": "left"}
    - symptom_search
* intensity{"intensity": "9"}
    - slot{"intensity": "9"}
    - action_intensity
* picking_specialty
    - utter_ask_doyouwantappointment
* affirm
    - utter_ask_location
* location_entry{"location": "Vegas"}
    - slot{"location": "Vegas"}
    - form_questions
    - form{"name": "form_questions"}
    - slot{"requested_slot": "name"}
* form: form_entry{"name": "Arushi Tyagi"}
    - slot{"name": "Arushi Tyagi"}
    - form: form_questions
    - slot{"name": "Arushi Tyagi"}
    - slot{"requested_slot": "phone"}
* form_entry{"phone": "9910576342"}
    - slot{"phone": "9910576342"}
    - action_check_number
    - form_questions
    - slot{"requested_slot": "age"}
* form: form_entry{"age": "19"}
    - slot{"age": "19"}
    - form: form_questions
    - slot{"age": "19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_doc_name
* affirm
    - utter_ask_doctor
* doc_name{"doctor": "Dr. Tyagi"}
    - slot{"doctor": "Dr. Tyagi"}
    - utter_appointment_maker
* pick_time
    - utter_appointment_made
    - summarize
    - utter_anything_else_icanhelpwith
    - utter_anything_else_icanhelpwith
* deny
    - utter_goodbye
## interactive_story_2
    * greet
      - utter_greet
    * sick
      - utter_im_sorry
      - form_questions
      - form{"name":"form_questions"}
      - form{"name":null}
      - utter_ask_symptoms
    * symptoms{"symptom": "leg pain"}
        - slot{"symptom": "leg pain"}
        - action_side
    * side{"side": "left"}
        - slot{"side": "left"}
        - symptom_search
    * intensity{"intensity": "9"}
        - slot{"intensity": "9"}
        - action_intensity
    * picking_specialty
        - utter_ask_doyouwantappointment
    * deny
        - utter_anything_else_icanhelpwith
    * deny
        - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## fallback story
* out_of_scope
  - action_default_fallback

## nearest service
  * greet
    -utter_greet
  * closest_thing
    - location_form
    - form{"name":"location_form"}
    - form{"name":null}
  * goodbye
    - utter_goodbye

## asking for Ambulance
  * greet
    - utter_greet
  * info_services
    - utter_ask_service
  * location_based_services{"service":"ambulance"}
    - utter_ask_location
  * location_entry
    - utter_service_response
## nearest service
* greet_with_name
  - utter_greet_name
* closest_thing
  - location_form
  - form{"name":"location_form"}
  - form{"name":null}
* goodbye
  - utter_goodbye

## asking for Ambulance
* greet_with_name
  - utter_greet_name
* info_services
  - utter_ask_service
* location_based_services{"service":"ambulance"}
  - utter_ask_location
* location_entry
  - utter_service_response
* affirm
  - utter_anything_else_icanhelpwith
* deny
  - utter_goodbye
## asking for Ambulance
  * greet_with_name
    - utter_greet_name
  * info_services
    - utter_ask_service
  * location_based_services{"service":"ambulance"}
    - utter_ask_location
  * location_entry
    - utter_service_response
  * affirm
    - utter_anything_else_icanhelpwith
  * affirm
    - utter_greet
## interactive_story_1
  * greet
      - utter_greet
  * closest_thing{"amenity": "hospital"}
      - slot{"amenity": "hospital"}
      - utter_ask_location
  * location_entry{"location": "California"}
      - action_place_search

## 1
  * sick
      - utter_im_sorry
      - form_questions
      - form{"name": "form_questions"}
      - form{"name":null}
      - utter_ask_symptoms
  * symptoms{"symptom": "leg pain"}
      - slot{"symptom": "leg pain"}
      - action_side
  * side{"side": "left"}
      - slot{"side": "left"}
      - symptom_search
  * intensity{"intensity": "9"}
      - slot{"intensity": "9"}
      - action_intensity
  * picking_specialty
      - utter_ask_doyouwantappointment
  * deny
      - utter_anything_else_icanhelpwith
  * deny
      - utter_goodbye


## sick
  * greet
      - utter_greet
  * sick
      - utter_im_sorry
      - form_questions
      - form{"name": "form_questions"}
      - form{"name":null}
      - utter_ask_symptoms
  * symptoms
      - action_side
  * side
      - symptom_search
  * intensity
      - action_intensity

## interactive_story_2
      * greet
          - utter_greet
      * sick
          - utter_im_sorry
          - form_questions
          - form{"name": "form_questions"}
          - slot{"requested_slot": "name"}
      * form: form_entry{"name": "Kajal Kapoor"}
          - slot{"name": "Kajal Kapoor"}
          - form: form_questions
          - slot{"name": "Kajal Kapoor"}
          - slot{"requested_slot": "phone"}
      * form: form_entry{"phone": "9810283041"}
          - slot{"phone": "9810283041"}
          - form: form_questions
          - slot{"phone": "9810283041"}
          - slot{"requested_slot": "age"}
      * form: form_entry{"age": "19"}
          - slot{"age": "19"}
          - form: form_questions
          - slot{"age": "19"}
          - form{"name": null}
          - slot{"requested_slot": null}
          - utter_ask_symptoms
      * symptoms{"symptoms": "headache and diziness"}
          - action_side
      * side
          - symptom_search
      * intensity{"intensity": "9"}
          - slot{"intensity": "9"}
          - action_intensity
      * picking_specialty{"specialty": "Cardiology"}

## interactive_story_1
  * greet
      - utter_greet
  * symptoms{"symptom": "headache"}
      - slot{"symptom": "headache"}
      - action_side
  * side
      - symptom_search
  * intensity{"intensity": "4"}
      - slot{"intensity": "4"}
      - action_intensity
  * picking_specialty
      - summarize
  * goodbye
      - utter_goodbye

## interactive_story_1
  * greet
      - utter_greet
  * symptoms{"symptom": "headache"}
      - slot{"symptom": "headache"}
      - action_side
  * side
      - symptom_search
  * intensity{"intensity": "4"}
      - slot{"intensity": "4"}
      - action_intensity
  * picking_specialty
      - summarize

## interactive_story_1
  * greet
      - utter_greet
  * make_appointment
      - form_questions
      - form{"name": "form_questions"}
      - slot{"requested_slot": "name"}
  * form: form_entry{"name": "Mehakpreet Kaur"}
      - slot{"name": "Mehakpreet Kaur"}
      - form: form_questions
      - slot{"name": "Mehakpreet Kaur"}
      - slot{"requested_slot": "phone"}
  * form: form_entry{"phone": "2017049762"}
      - slot{"phone": "2017049762"}
      - form: form_questions
      - slot{"phone": "2017049762"}
      - slot{"requested_slot": "age"}
  * form: form_entry{"age": "21"}
      - slot{"age": "21"}
      - form: form_questions
      - slot{"age": "21"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - utter_ask_doc_name
  * doc_name{"doctor": "Dr. Tyagi"}
      - utter_appointment_maker
  * pick_time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith
    * deny
      - utter_goodbye

## interactive_story_1
      * make_appointment
          - form_questions
          - form{"name": "form_questions"}
          - slot{"requested_slot": "name"}
      * form: form_entry{"name": "Mehakpreet Kaur"}
          - slot{"name": "Mehakpreet Kaur"}
          - form: form_questions
          - slot{"name": "Mehakpreet Kaur"}
          - slot{"requested_slot": "phone"}
      * form: form_entry{"phone": "2017049762"}
          - slot{"phone": "2017049762"}
          - form: form_questions
          - slot{"phone": "2017049762"}
          - slot{"requested_slot": "age"}
      * form: form_entry{"age": "21"}
          - slot{"age": "21"}
          - form: form_questions
          - slot{"age": "21"}
          - form{"name": null}
          - slot{"requested_slot": null}
          - utter_ask_doc_name
      * doc_name{"doctor": "Dr. Tyagi"}
          - utter_appointment_maker
      * pick_time
          - utter_appointment_made
          - summarize
          - utter_anything_else_icanhelpwith
        * affirm
          - utter_greet

## 2
  * greet
    - utter_greet
  * symptoms
    - utter_im_sorry
    - form{"name":"form_questions"}
    - form{"name":null}
    - symptom_search
  * intensity
    - action_intensity
  * picking_specialty
    - summarize
    - utter_ask_doyouwantappointment
  * affirm
    - utter_ask_location
  * location_entry
    - utter_ask_doc_name
  * doc_name
    - utter_appointment_maker
  * time
    - utter_appointment_made
    - summarize
    - utter_anything_else_icanhelpwith

## 3
  * greet
    - utter_greet
  * sick
    - utter_im_sorry
    - form{"name":"form_questions"}
    - form{"name":null}
    - action_check_number
    - utter_ask_symptoms
  * symptoms
    - symptom_search
  * intensity
    - action_intensity
  * picking_specialty
    - utter_ask_doyouwantappointment
  * affirm
    - utter_ask_location
  * location_entry
    - utter_ask_doc_name
  * doc_name
    - utter_appointment_maker
  * time
    - utter_appointment_made
    - summarize
    - utter_anything_else_icanhelpwith


## story 3
* greet
  - utter_greet
* sick
  - utter_im_sorry
  - form_questions
  - form{"name":"form_questions"}
  - form{"name":null}
  - utter_ask_symptoms
* symptoms{"symptom": "leg pain"}
    - slot{"symptom": "leg pain"}
    - action_side
* side{"side": "left"}
    - slot{"side": "left"}
    - symptom_search
* intensity{"intensity": "9"}
    - slot{"intensity": "9"}
    - action_intensity
* picking_specialty
    - utter_ask_doyouwantappointment
* affirm
    - utter_ask_location
* location_entry{"location": "Vegas"}
    - slot{"location": "Vegas"}
    - utter_ask_doc_name
* affirm
    - utter_ask_doctor
* doc_name{"doctor": "Dr. Tyagi"}
    - slot{"doctor": "Dr. Tyagi"}
    - utter_appointment_maker
* pick_time
    - utter_appointment_made
    - summarize
    - utter_anything_else_icanhelpwith

## interactive_story_1
* greet
    - utter_greet
* make_appointment
    - form_questions
    - form{"name":"form_questions"}
    - form{"name":null}
    - utter_ask_doctor
* doc_name{"doctor": "Dr. Rakesh"}
    - slot{"doctor": "Dr. Rakesh"}
    - utter_ask_symptoms
* symptoms{"symptom": "headache"}
    - slot{"symptom": "headache"}
    - action_side
    - symptom_search
* intensity{"intensity": "7"}
    - slot{"intensity": "7"}
    - utter_appointment_maker
* pick_time
    - utter_appointment_made
## 2
* greet
  - utter_greet
* make_appointment
  - form_questions
  - form{"name":"form_questions"}
  - form{"name":null}
  - utter_ask_doctor



## interactive_story_1
    * greet_with_name
      - utter_greet_name
    * make_appointment
        - form_questions
        - form{"name": "form_questions"}
        - slot{"requested_slot": "name"}
    * form: form_entry{"name": "Mehakpreet Kaur"}
        - slot{"name": "Mehakpreet Kaur"}
        - form: form_questions
        - slot{"name": "Mehakpreet Kaur"}
        - slot{"requested_slot": "phone"}
    * form: form_entry{"phone": "2017049762"}
        - slot{"phone": "2017049762"}
        - form: form_questions
        - slot{"phone": "2017049762"}
        - slot{"requested_slot": "age"}
    * form: form_entry{"age": "21"}
        - slot{"age": "21"}
        - form: form_questions
        - slot{"age": "21"}
        - form{"name": null}
        - slot{"requested_slot": null}
        - utter_ask_doc_name
    * doc_name{"doctor": "Dr. Tyagi"}
        - utter_appointment_maker
    * pick_time
        - utter_appointment_made
        - summarize
        - utter_anything_else_icanhelpwith
      * deny
        - utter_goodbye

## interactive_story_1
        * make_appointment
            - form_questions
            - form{"name": "form_questions"}
            - slot{"requested_slot": "name"}
        * form: form_entry{"name": "Mehakpreet Kaur"}
            - slot{"name": "Mehakpreet Kaur"}
            - form: form_questions
            - slot{"name": "Mehakpreet Kaur"}
            - slot{"requested_slot": "phone"}
        * form: form_entry{"phone": "2017049762"}
            - slot{"phone": "2017049762"}
            - form: form_questions
            - slot{"phone": "2017049762"}
            - slot{"requested_slot": "age"}
        * form: form_entry{"age": "21"}
            - slot{"age": "21"}
            - form: form_questions
            - slot{"age": "21"}
            - form{"name": null}
            - slot{"requested_slot": null}
            - utter_ask_doc_name
        * doc_name{"doctor": "Dr. Tyagi"}
            - utter_appointment_maker
        * pick_time
            - utter_appointment_made
            - summarize
            - utter_anything_else_icanhelpwith
          * affirm
            - utter_greet
## 2
  * greet_with_name
    - utter_greet_name
    * symptoms
      - utter_im_sorry
      - form{"name":"form_questions"}
      - form{"name":null}
      - symptom_search
    * intensity
      - action_intensity
    * picking_specialty
      - summarize
      - utter_ask_doyouwantappointment
    * affirm
      - utter_ask_location
    * location_entry
      - utter_ask_doc_name
    * doc_name
      - utter_appointment_maker
    * time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith

## 3
    * greet_with_name
      - utter_greet_name
    * sick
      - utter_im_sorry
      - form{"name":"form_questions"}
      - form{"name":null}
      - action_check_number
      - utter_ask_symptoms
    * symptoms
      - symptom_search
    * intensity
      - action_intensity
    * picking_specialty
      - utter_ask_doyouwantappointment
    * affirm
      - utter_ask_location
    * location_entry
      - utter_ask_doc_name
    * doc_name
      - utter_appointment_maker
    * time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith


## story 3
  * greet_with_name
    - utter_greet_name
  * sick
    - utter_im_sorry
    - form_questions
    - form{"name":"form_questions"}
    - form{"name":null}
    - utter_ask_symptoms
  * symptoms{"symptom": "leg pain"}
      - slot{"symptom": "leg pain"}
      - action_side
  * side{"side": "left"}
      - slot{"side": "left"}
      - symptom_search
  * intensity{"intensity": "9"}
      - slot{"intensity": "9"}
      - action_intensity
  * picking_specialty
      - utter_ask_doyouwantappointment
  * affirm
      - utter_ask_location
  * location_entry{"location": "Vegas"}
      - slot{"location": "Vegas"}
      - utter_ask_doc_name
  * affirm
      - utter_ask_doctor
  * doc_name{"doctor": "Dr. Tyagi"}
      - slot{"doctor": "Dr. Tyagi"}
      - utter_appointment_maker
  * pick_time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith

## interactive_story_1
  * greet_with_name
    - utter_greet_name
  * make_appointment
      - form_questions
      - form{"name":"form_questions"}
      - form{"name":null}
      - utter_ask_doctor
  * doc_name{"doctor": "Dr. Rakesh"}
      - slot{"doctor": "Dr. Rakesh"}
      - utter_ask_symptoms
  * symptoms{"symptom": "headache"}
      - slot{"symptom": "headache"}
      - action_side
      - symptom_search
  * intensity{"intensity": "7"}
      - slot{"intensity": "7"}
      - utter_appointment_maker
  * pick_time
      - utter_appointment_made
      - summarize
      - utter_anything_else_icanhelpwith
## 2
  * greet_with_name
    - utter_greet_name
  * make_appointment
    - form_questions
    - form{"name":"form_questions"}
    - form{"name":null}
    - utter_ask_doctor

## service
    * greet
      - utter_greet
    * doc_info
      - utter_ask_doctor
    * doc_name
      - utter_doc_info
      - utter_anything_else_icanhelpwith
    * affirm
      - utter_greet
    * sick
      - utter_im_sorry
      - form_questions
      - form{"name":"form_questions"}
      - form{"name":null}
      - utter_ask_symptoms

## service
* greet
  - utter_greet
* doc_info
  - utter_ask_doctor
* doc_name
  - utter_doc_info
  - utter_anything_else_icanhelpwith
## service
  * greet
    - utter_greet
  * doc_info_with_name
    - utter_doc_info
    - utter_anything_else_icanhelpwith

## interactive_story_1
* greet
    - utter_greet
* doc_info{"doctor": "Dr. Tyagi"}
    - slot{"doctor": "Dr. Tyagi"}
    - utter_doc_info
    - utter_anything_else_icanhelpwith
* deny
    - utter_goodbye
