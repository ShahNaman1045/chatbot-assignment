# AI Chatbot Assignment

This project is a simple AI-powered chatbot built as part of an assignment.

It uses a **React frontend** and a **FastAPI backend** connected to an **OpenAI language model**.  
The chatbot analyzes user input and responds with different behaviors depending on the message type.

---

## Live Demo

Frontend (Vercel):  
https://chatbot-assignment-ten.vercel.app/

Backend API Docs:  
https://chatbot-assignment-oa1s.onrender.com/docs

---

## Project Architecture

Frontend (React) → Backend (FastAPI) → OpenAI API

```
User
 ↓
React App (Vercel)
 ↓
FastAPI Backend (Render)
 ↓
OpenAI LLM
```

---

## Features

### 1. Task + Deadline Detection

If a user enters a task with a deadline, the chatbot colors the response depending on how soon the deadline is.

| Time Remaining | Color |
|---|---|
≥ 24 hours | Blue |
12–24 hours | Yellow |
< 2 hours | Orange |

Example input:

```
Finish the report tomorrow
```

---

### 2. Random Number Input

If the user enters a random number, the chatbot colors the response depending on the **last two digits**.

| Last Two Digits | Color |
|---|---|
00 | White |
≤ 50 | Grey |
> 50 | Black |

Example input:

```
45892
```

---

### 3. Sentiment-Based Response

For normal text messages, the chatbot analyzes the tone of the message and colors the response accordingly.

| Sentiment | Color |
|---|---|
Very sad | Red |
Somewhat sad | Light Red |
Neutral | Amber |
Happy | Green |

Example input:

```
I feel terrible today
```

---

### 4. Political Leader Persona

All chatbot responses:

- Are written **in another language (Spanish)**  
- Include an **English translation**  
- Are generated **as if responding from a political leader**

Example response:

```
Spanish:
Gracias por tu mensaje. Nuestro compromiso es servir al pueblo con dedicación.

English:
Thank you for your message. Our commitment is to serve the people with dedication.
```

---

### 5. Authentication Guardrail

Only users with the email domain:

```
@petasight.com
```

are allowed to interact with the chatbot.

Other email domains are rejected.

---

### 6. Accessibility (WCAG-2.0)

The UI includes accessibility considerations such as:

- Adequate color contrast
- Keyboard support (Enter key to send message)
- ARIA labels for input fields

---

## Tech Stack

Frontend
- React.js
- Axios

Backend
- FastAPI
- Python

AI / NLP
- OpenAI API
- VADER Sentiment Analysis

Deployment
- Vercel (Frontend)
- Render (Backend)

---

## Running the Project Locally

### 1. Start Backend

Navigate to backend folder:

```
cd backend
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### 2. Start Frontend

Navigate to frontend folder:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start the app:

```
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## Environment Variables

Create a `.env` file in the backend directory:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## Tools Used

During development the following tools were used:

- VS Code
- Git & GitHub
- React
- FastAPI
- OpenAI API
- Render (backend hosting)
- Vercel (frontend hosting)

---

## Thinking Process

The assignment was approached in the following steps:

1. Break down the problem into three classifications:
   - task with deadline
   - random number input
   - sentiment-based message

2. Implement rule-based logic in the backend to determine the correct response color.

3. Use an LLM to generate responses in a **political leader persona**, returning both **Spanish and English translations**.

4. Build a simple accessible React chat interface.

5. Deploy the backend on Render and the frontend on Vercel.

---

## Author

Naman Shah
