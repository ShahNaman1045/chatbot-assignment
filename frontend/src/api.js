import axios from "axios"

const API_URL = "https://chatbot-assignment-oa1s.onrender.com/chat"

export const sendMessage = async (message, email) => {

  const res = await axios.post(API_URL, {
    message,
    email,
  })

  return res.data
}