import React from 'react';
import './Block.css'

interface BlockProps {
  value: string,
  isActive: boolean,
  isSelected: boolean;
  onMouseDown: () => void;
  onMouseEnter: () => void;
  onMouseUp: () => void;
}

const Block: React.FC<BlockProps> = ({ value, isActive, isSelected, onMouseDown, onMouseEnter, onMouseUp }) => {
  return (
    <>
      { isActive ?
        <div
          onMouseDown={isActive && onMouseDown}
          onMouseEnter={onMouseEnter}
          onMouseUp={onMouseUp}
          className={`grid-item ${isSelected ? 'selected' : 'default'}`}
        >
          {value}
        </div> :
        <div
          className={`grid-item green`}
        >
          {value}
        </div>
      }

    </>
  );
};

export default Block;
