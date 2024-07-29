# Fillwords Game 🎨

Welcome to the Fillwords Game repository! This document provides an overview of the project, including the algorithm, backend, and frontend components, along with instructions for running the project locally.

## Personal Note 💬

I really enjoy playing Fillwords, so I decided to create my own version with dynamic and random generation. I hope you enjoy it as much as I do! 😊

## Part 1: Algorithm 🧩

The algorithm for generating the Fillwords game board involves several steps:

1. **Word Count Calculation**: The algorithm calculates and selects the number of words to fit on the board based on its size.

2. **Word Length Array Generation**: An array of word lengths is generated using `itertools.product`.

3. **Word Selection**: Words of appropriate length are randomly selected from pre-parsed files.

4. **Word Placement**: Starting positions for words on the board are randomly determined. A Depth-First Search (DFS) algorithm with random parent choices is used to place the words on the board. This process continues until a `size x size` board is generated.

5. **Output**: The algorithm returns both the generated board and the list of words used.

## Part 2: Backend 🚀

The backend is implemented using **FastAPI** and exposes a single route:

- **`/getWords/{size}`**: This route generates and returns a game board of the specified size along with the answers.

### Running the Backend

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vadimcha/FillwordsGame.git
   ```

2. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

3. **Create and activate a virtual environment**:
   - On macOS and Linux:
     ```bash
     python3 -m venv ven
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python3 -m venv ven
     .\venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Parse words of length 4 to 10**:
   ```bash
   python3 parser.py
   ```

6. **Run the FastAPI server**:
   ```bash
   fastapi dev main.py
   ```

## Part 3: Frontend 🌐

The frontend is built with **ReactJS**.

### Running the Frontend

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the client**:
   ```bash
   npm run dev
   ```

4. **Access the website**: The site will be available at [http://localhost:5173/](http://localhost:5173/).
