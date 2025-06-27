import { useState } from 'react'
import axios from 'axios'

function App() {
  const [pregunta, setPregunta] = useState('')
  const [respuesta, setRespuesta] = useState('')
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState('')

  const enviarPregunta = async () => {
    if (!pregunta.trim()) return
    setCargando(true)
    setError('')
    setRespuesta('')

    try {
      const res = await axios.post('http://localhost:8000/query', {
        pregunta,
      })
      setRespuesta(res.data.respuesta)
    } catch (err) {
      setError('Hubo un error al consultar el backend.')
      console.log(err);
    } finally {
      setCargando(false)
    }
  }

  return (
    <div style={{ maxWidth: 600, margin: '0 auto', padding: 20}}>
      <h1>Chat</h1>
      <textarea
        rows="4"
        value={pregunta}
        onChange={(e) => setPregunta(e.target.value)}
        placeholder="Escribe tu pregunta aquí..."
        style={{ width: '100%', padding: 10 }}
      />
      <button onClick={enviarPregunta} disabled={cargando}>
        {cargando ? 'Cargando...' : 'Enviar'}
      </button>

      {respuesta && (
        <div style={{ marginTop: 20, border: '1px solid #ffffff', padding: 10 }}>
          <h3>Respuesta:</h3>
          <p>{respuesta.toString()}</p>
        </div>
      )}

      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  )
}

export default App
