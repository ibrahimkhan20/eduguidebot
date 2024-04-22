#main code
import openai
import gradio
import time

openai.api_key = "INSERT OPEN AI KEY HERE"
#IN ORDER TO GENERATE A KEY, PLEASE VISIT https://openai.com/blog/openai-api AND CREATE AN ACCOUNT TO ACCESS THE API FEATURES.
#I HAD TO REMOVE MY PRIVATE API KEY AS IT WILL FINANCIALLY IMPACT MYSELF.

messages = [{"role": "system", "content": "You are a chatbot called EduGuideBot, that aims to solve university questions from Aston university.Also, remember that New Students start 18 September 2023, Returning Students start 25 September 2023, First Term End on 16 December 2023. Second Term is between 8 January 2024 to 28 March 2024. Third Term is between 22 April 2024 to 8 June 2024. Summer Degree Congregations are 16 July 2024 to 25 July 2024, and Referred Examinations are 19 to 24 August 2024. Also, remember that the results for term 1 may be delayed by 2-3 days."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    
    # Add a visual cue for processing
    time.sleep(0.5)  # Simulating processing time
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Custom JavaScript for enhanced UI
js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Welcome student, please ask away...'; // welcome message for user
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}

"""

# Create Gradio interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="EduGuideBot - Aston University", 
                        description="Ask any questions related to Aston University.", 
                        allow_flagging=False, theme="huggingface", css=None, 
                        js=js)  # Inject custom JavaScript

# Launch the interface
shareable_link = demo.launch(share=True)
print("Shareable link:", shareable_link)

