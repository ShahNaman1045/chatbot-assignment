export default function MessageBubble({ text, color }) {
  return (
    <div className="message" style={{ backgroundColor: color }}>
      {text.split("\n").map((line, i) => (
        <p key={i}>{line}</p>
      ))}
    </div>
  )
}
