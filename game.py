import pandas as pd
import numpy as np
import streamlit as st
import time

# imports a static solved list
# info = pd.read_csv('Static_gamelist.csv')
info = pd.read_csv('Game1_Game2.csv', index_col=0)

# st.write(f'Top line is {info.iloc[0]}')

st.write('Welcome, Agent, to the Halloween Spy Game.')
# if st.button('Join Next game'):
#     st.write('Enter your country and passphrase to access your dossier.')
#     identity = st.text_input('Country',key='Pakistan')
#     if identity:
#         st.write("Why don't you work")
    # passphrase = st.text_input('Passphrase')
    # val = info[info.Country == country]['Passphrase']
    # print(val)
    # if st.write('test'):
    #     st.write('Credentials Accepted. Loading Secure Terminal. Please ensure you were not followed.')

number = 7 
guess = st.text_input(f"Enter your country to present your credentials to the gala security.",key=number)
if guess:
    try:
        st.write(f'(Not included in game) Passphrase is {info[info.Country == guess]['Passphrase'].values[0]}')
        passphrase = info[info.Country == guess]['Passphrase'].values[0]
        challenge = st.text_input(f"Now enter your passphrase to access your dossier",key=6)
        if challenge:
            try:
                if challenge == passphrase:
                    st.write(f'Credentials accepted. Welcome, {info[info.Country == guess]['AgentName'].values[0]}.')
                    if st.button('Full Mission Briefing'):
                        time.sleep(1)
                        st.write('Your mission details are as follows.')
                        time.sleep(3)
                        st.write('You are a guest at the Halloween gala of a reclusive industrial tycoon. Numerous dignitaries, celebrities, and delegates of national governments are in attendance. Beneath the surface, however, many of your costumed acquaintances wear a second mask - they are secret agents carrying out the orders of their secretive private agencies.')
                        time.sleep(5)
                        st.write(f"You are posing as a minor government official from the country of {info[info.Country == guess]['Country'].values[0]}. In reality, you, too, are a secret agent, sent to locate and expose another enemy agent before they can commit grave damage to your homeland.")
                        time.sleep(5)
                        st.write(f"Your target is {info[info.Country == guess]['Target'].values[0]}. Our sources could not determine which delegate {" ".join(info[info.Country == guess]['Target'].values[0].split(' ')[-2:])} is pretending to be. Your mission is to find out - determine which country your target is hiding behind, confront them, and publicly declare their identity to remove them from the game.  If you’re right, take their card. You now have their secret information.")
                        time.sleep(3)
                        st.write("Anyone can expose an agent's identity. However, you can only remove someone from the game if you have the card (or dossier passphrase) naming them as a target. In other words, if you take out your target, you inherit their own target - and can expose them next.")
                        time.sleep(5)
                        st.write('But be cautious - you are being hunted at the same time. Someone at this party is trying to track you down and give you the same treatment.')
                        time.sleep(3)
                        st.write(f"Fortunately, while we don't know your target's cover identity, our research did uncover the secret identities of two other guests at this party:")
                        st.write(info[info.Country == guess]['FirstContact'].values[0])
                        st.write(info[info.Country == guess]['SecondContact'].values[0])
                        time.sleep(3)
                        st.write(f"You may use this knowledge any way you can think of to obtain intelligence about your own target. Blackmail these agents, team up with them, trade their identities to other hidden agents, or 'burn' them by exposing their identities to their own pursuers. You can even trade your own secret identity and target, if you dare.")
                        time.sleep(6)
                        st.write(f"You'll need all of your wits and training to pull this mission off. Good luck, {info[info.Country == guess]['AgentName'].values[0]}. Message ends.")
                    if st.button('Key Mission Details'):
                        st.write(f'Your target is {info[info.Country == guess]['Target'].values[0]}')
                        st.write(f'Secret identities provided to you by HQ:')
                        st.write(info[info.Country == guess]['FirstContact'].values[0])
                        st.write(info[info.Country == guess]['SecondContact'].values[0])  
                        st.write('Remember, someone is targeting you!')
                else:
                    st.write('Incorrect. This message will self destruct in 5...')
                    time.sleep(1)
                    st.write('4...')
                    time.sleep(1)
                    st.write('3...')
                    time.sleep(1)
                    st.write('2...')
                    time.sleep(1)
                    st.write('1...')
                    time.sleep(2)
                    st.write('....1/2.....')
                    time.sleep(2)
                    st.write("...Hm, that's odd. The self-destruct should have worked. Anyways, please try again.")
            except Exception as e:
                st.write('enter a correct passphrase')
            # st.write('you guessed it')
        else:
            st.write('Loading terminal...')
    except TypeError():
        st.write('Enter a valid country')

