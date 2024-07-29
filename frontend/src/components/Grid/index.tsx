import React, {useState, useCallback} from 'react';
import Block from '../Block';
import './Grid.css'

interface GridProps {
  answers: string[],
  dictionary: Array<string[]>
}


const Grid: React.FC<GridProps> = ({ answers, dictionary }) => {
  const [isMouseDown, setIsMouseDown] = useState(false);
  const [selectedBlocks, setSelectedBlocks] = useState<string[]>([]);
  const [word, setWord] = useState<string[]>([]);
  const size = dictionary.length
  const [isActive, setIsActive] = useState(Array.from({ length: size }, () => Array.from({ length: size }, () => true)))

  const handleMouseDown = useCallback((x: number, y: number, value: string) => {
    setIsMouseDown(true);
    selectBlock(x, y, value);
  }, []);

  const handleMouseEnter = useCallback((x: number, y: number, value: string) => {
    if (isMouseDown) {
      selectBlock(x, y, value);
    }
  }, [isMouseDown]);


  const rightAnswer = useCallback(() => {
    selectedBlocks.forEach(block => {
      const [x, y] = block.split('-').map(Number);
      setIsActive(prevState => {
        const copy = prevState
        copy[x][y] = false
        return copy
      })
    });
  }, [isActive, selectedBlocks])

  const handleMouseUp = useCallback(() => {
    setIsMouseDown(false);
    if(answers.indexOf(word.join('')) != -1) rightAnswer()
    setSelectedBlocks([])
    setWord([])
  }, [answers, rightAnswer, word]);


  const selectBlock = (x: number, y: number, value: string) => {
    setSelectedBlocks(prev => [...prev, `${x}-${y}`]);
    setWord(prev => [...prev, value])
  };

  const getBlockKey = (x: number, y: number) => `${x}-${y}`;

  return (
    <div className={"grid-container"} style={{ gridTemplateColumns: `repeat(${size}, 50px)` }}>
      {dictionary.map((row, x) =>
        row.map((value, y) => (
          <Block
            key={getBlockKey(x, y)}
            value={value}
            isActive={isActive[x][y]}
            isSelected={selectedBlocks.indexOf(`${x}-${y}`, 0) != -1}
            onMouseDown={() => handleMouseDown(x, y, value)}
            onMouseEnter={() => handleMouseEnter(x, y, value)}
            onMouseUp={handleMouseUp}
          />
        ))
      )}
    </div>
  );
};

export default Grid;
