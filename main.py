import streamlit as st
import yagmail
import os
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL = os.getenv("notwxli@gmail.com")
APP_PASSWORD = os.getenv("lhzl mqlf wpii kvnd")

st.title("Claim your reward/roles below!")

# Step tracking
if "step" not in st.session_state:
    st.session_state.step = 1

# Step 1: Choose application type
application = st.selectbox('Select:', ["Role create", "Reward Claim", "Others"])

if st.session_state.step == 1 and st.button('Confirm'):
    st.session_state.application = application
    if application in ["Role create", "Reward Claim", "Others"]:
        st.session_state.step = 2

# Step 2: Form input
if st.session_state.step == 2:
    if st.session_state.application == "Role create":
        name = st.text_input("Enter your Discord username:")
        if name and st.button('Next'):
            st.session_state.name = name
            st.session_state.step = 3

    elif st.session_state.application == "Reward Claim":
        username = st.text_input("Enter your Discord username:")
        reward = st.text_input("Enter the reward you want to claim:")

        if username and reward and st.button("Submit"):
            submission_id = str(uuid.uuid4())
            st.success("✅ Your reward claim has been sent to Developers. Wait for their reply.")
            st.info(f"Your submission ID: {submission_id}")

            # Send email
            try:
                yag = yagmail.SMTP('notwxli@gmail.com', 'lhzl mqlf wpii kvnd')
                yag.send(
                    to="walimps6112@gmail.com",  # change to your developer email
                    subject=f"New Reward Claim - ID {submission_id}",
                    contents=f"""
New Reward Claim

Submission ID: {submission_id}
Discord Username: {username}
Requested Reward: {reward}
"""
                )
                st.success("Developers have been notified successfully!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")

    elif st.session_state.application == "Others":
        other_request = st.text_area("Enter your request:")
        if other_request and st.button("Submit"):
            submission_id = str(uuid.uuid4())
            st.success("✅ Your request has been sent to Developers. Wait for their reply.")
            st.info(f"Your submission ID: {submission_id}")

            # Send email
            try:
                yag = yagmail.SMTP('notwxli@gmail.com', 'lhzl mqlf wpii kvnd')
                yag.send(
                    to="walimps6112@gmail.com",  # change to your developer email
                    subject=f"New General Request - ID {submission_id}",
                    contents=f"""
New General Request

Submission ID: {submission_id}
Request Details:
{other_request}
"""
                )
                st.success("Developers have been notified successfully!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")

# Step 3 & 4: Role create workflow remains the same
if st.session_state.step == 3 and st.session_state.application == "Role create":
    invites = st.radio("1. Have you made at least 2 invitations to the Discord server?", ['Yes', 'No'])
    if st.button("Next"):
        if invites == "No":
            st.warning("Pass — you need at least 2 invitations to continue.")
        else:
            st.session_state.invites = invites
            st.session_state.step = 4

if st.session_state.step == 4 and st.session_state.application == "Role create":
    usernames = st.text_area("2. Enter their Discord usernames (one per line):")
    role_name = st.text_input("3. Name the role you want to create:")

    if st.button("Submit"):
        if len(role_name.strip()) > 3:
            submission_id = str(uuid.uuid4())
            st.session_state.submission_id = submission_id

            st.success("✅ Your answers have been sent to Developers. Wait for their reply.")
            st.info(f"Your submission ID: {submission_id}")

            # Send email (optional)
            try:
                yag = yagmail.SMTP('notwxli@gmail.com', 'lhzl mqlf wpii kvnd')
                yag.send(
                    to="walimps6112@gmail.com",
                    subject=f"New Role Create Request - ID {submission_id}",
                    contents=f"""
New Role Creation Request

Submission ID: {submission_id}
Discord Username: {st.session_state.name}
Invited Members:
{usernames}
Requested Role Name: {role_name}
"""
                )
                st.success("Developers have been notified successfully!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")

        else:
            st.warning("Pass — role name must be longer than 3 letters.")
