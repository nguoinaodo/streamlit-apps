import streamlit as st
import numpy as np
import pandas as pd

# Sudoku Solver Algorithm (backtracking)
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in board[:, col]:
        return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num
                        if solve(board):
                            return True
                        board[row, col] = 0
                return False
    return True

# Function to display the Sudoku board as a pandas DataFrame
def board_to_dataframe(board):
    return pd.DataFrame(board).astype(str).replace("0", "")

# Streamlit app interface
def main():
    st.title("Sudoku Solver with Editable Table")

    st.write("""
    ### Enter your Sudoku puzzle
    You can edit the table directly. Fill in the Sudoku puzzle with numbers from 1-9 and leave empty cells as blank (or 0).
    """)

    # Create a 9x9 empty Sudoku grid with zeros
    board = np.zeros((9, 9), dtype=int)

    # Create the table as an editable dataframe
    editable_df = pd.DataFrame(board, dtype=int)

    # Use st.data_editor for user input
    edited_board = st.data_editor(
        editable_df,
        column_config={
            col: st.column_config.NumberColumn() for col in editable_df.columns
        },
        use_container_width=True,
    )

    # Convert the edited DataFrame to a numpy array (board)
    updated_board = edited_board.to_numpy()

    # Button to solve the Sudoku
    if st.button('Solve Sudoku'):
        if solve(updated_board):
            st.success("Solved Sudoku")
            solved_board_df = board_to_dataframe(updated_board)
            st.table(solved_board_df)  # Display the solved board
        else:
            st.error("No solution found! Please check your puzzle.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
