import random
import streamlit as st

# Setting the title and subtitle
st.title("🎮 Rock-Paper-Scissors Game 🎮")
st.subheader("Challenge the computer and see who wins!")


st.write("Choose wisely:")
user_choice = st.radio("Pick one:", ["Rock", "Paper", "Scissor"])

choices = ["Rock", "Paper", "Scissor"]
user_choice_name = user_choice

# Random choice for computer
comp_choice = random.choice(choices)
comp_choice_name = comp_choice

# Display choices
st.write(f"**Your choice:** {user_choice_name}")
st.write(f"**Computer's choice:** {comp_choice_name}")

# Determine the winner
if user_choice_name == comp_choice_name:
    st.write("It's a draw! 🤝")
elif (user_choice_name == "Rock" and comp_choice_name == "Scissor") or \
     (user_choice_name == "Scissor" and comp_choice_name == "Paper") or \
     (user_choice_name == "Paper" and comp_choice_name == "Rock"):
    st.write("You Win! 🎉")
else:
    st.write("You lose! 💔")

# Adding a play again button
if st.button('Play Again'):
    st.experimental_set_query_params(restart=str(random.randint(0, 10000)))
