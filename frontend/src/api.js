import axios from "axios"

const API_URL = "http://localhost:8000/chat"

export const sendMessage = async (message, email) => {

  const res = await axios.post(API_URL, {
    message,
    email,
  })

  return res.data
}