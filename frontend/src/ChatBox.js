import { useState } from "react";
import { sendMessage } from "./api";
import MessageBubble from "./MessageBubble";

export default function ChatBox() {
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");
    const [messages,setMessages] = useState([]);

    const handleSend = async () => {
        const data = await sendMessage(message, email);

        if (data.error) {
            alert(data.error);
            return;
        }

        setMessages([
            ...messages,
            {text:data.response, color:data.color}
        ]);

        setMessage("");
    }

    return(
    <div>

      <label htmlFor="email">Email: </label>
      <input
        id="email"
        aria-label="email input"
        type="email"
        placeholder="Enter email"
        value={email}
        onChange={(e)=>setEmail(e.target.value)}
      />

      <div className="chat-header">
        AI Chat Assistant
      </div>

      <div className="chat-container">
        {messages.map((msg, i) => (
            <MessageBubble
            key={i}
            text={msg.text}
            color={msg.color}
            />
        ))}
      </div>

      <div className="input-row">

      <input
        aria-label="chat message input"
        placeholder="Type message"
        value={message}
        onChange={(e)=>setMessage(e.target.value)}
        onKeyDown={(e)=>{
            if(e.key==="Enter"){
            handleSend()
            }
        }}
        />

        <button onClick={handleSend}>Send</button>

        </div>

    </div>
  )
}
