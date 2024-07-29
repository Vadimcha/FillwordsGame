import './index.css'
import Grid from "./components/Grid";
import {useState} from "react";
import axios from 'axios';

const App = () => {
  const [isData, setIsData] = useState<boolean>(false)
  const [answers, setAnswers] = useState<string[]>([])
  const [dictionary, setDictionary] = useState<Array<string[]>>([])
  const getData = () => {
    axios.get("http://127.0.0.1:8000/getWords/5")
      .then((res) => {
        setAnswers(res.data.answers)
        setDictionary(res.data.dictionary.map((row: string) => row.split('')))
        setIsData(true)
      })
      .catch((error) => {
        console.log(error);
      });
  }
  return (
    <>
      {
      isData ?
        <div>
          <Grid answers={answers} dictionary={dictionary}/>
        </div> :
        <button onClick={() => getData()}>Начать игру</button>
      }
    </>
  );
};

export default App;