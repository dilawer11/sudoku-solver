<template>
  <div class="sudoku-solver">
    <p>{{msg}}</p>
    <div v-if="!optionSelected">
      <button @click="play">Play A Level</button>
      <button @click="solve">Solve Board</button>
    </div>
    <div v-else>
      <div id="board" class="board">
        <ul v-if="board">
          <li v-for="i in boardSize * boardSize" :key="i">
            <span>{{sudokuBoard[Math.floor((i - 1) / boardSize)][(i - 1) % boardSize]}}</span>
            <!-- <span>{{getValue(i)}}</span> -->
          </li>
          <!-- <li><span>9</span></li> -->
        </ul>
      </div>
      <button @click="back">Back</button>
      <div v-if="optionSelected=='solve'">
        <button @click="goBackPlaces(5)">Go Back 5 Places</button>
        <button @click="solveBoard()">Solve</button>
      </div>
      
      <button v-if="optionSelected=='play'">Check</button>
    </div>
  </div>
</template>
<script>
import Vue from 'vue'
export default {
  name: 'SudokuSolver',
  data () {
    return {
      msg: 'Welcome to Sudoku Solver',
      optionSelected: null,
      board: null,
      boardSize: 9,
      stack: [],
      storedboard:[
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 7],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 6, 0, 7, 9]
    ]
    }
  },
  methods:{
    getValue(i){
      i--;
      console.log(i)
      var c = i % this.boardSize
      var r = Math.floor(i / this.boardSize)
      console.log(r, c)
      if(this.board[r][c]){
        return this.board[r][c]
      }else{
        return 
      }
    },
    async goBackPlaces(p){
      for(var i = 0; i < p; i++){
        var st = this.stack.length - 1;
        var r = this.stack[st][0]
        var c = this.stack[st][1]
        this.stack.pop()
        Vue.set(this.board[r], c, null)
        await this.sleep(100)
      }
    },
    copyBoard(){
      for(var r = 0; r < this.boardSize; r++){
        for (var c = 0; c < this.boardSize; c++){
          if(this.storedboard[r][c]){
            this.board[r][c] = this.storedboard[r][c];
          } else{
            this.board[r][c] = null;
          }
        }
      }
    },
    play(){
      this.optionSelected = "play"
      this.msg = "PLAY"
      // this.copyBoard()
    },
    solve(){
      this.optionSelected = "solve"
      this.msg = "SOLVE"
      this.copyBoard()
      // this.board = this.storedboard
    },
    back(){
      this.optionSelected = null
      this.msg = 'Welcome to Sudoku Solver'
      // clear everything
    },
    sleep(milliseconds){
      return new Promise(resolve => setTimeout(resolve, milliseconds))
    },
    rollback(){
      if (!this.stack.length){
          console.log('Unsolvable')
          return [9, 9]
      }
      var stackTop = this.stack.length - 1
      var row = this.stack[stackTop][0]
      var col = this.stack[stackTop][1]
      var currentValue = this.board[row][col]
      this.board[row][col] = null
      this.stack.pop()
      for (var i = currentValue + 1; i <= this.boardSize; i++){
        if (this.insertValid(row, col, i)){
          // this.board[row][col] = i
          Vue.set(this.board[row], col, i)
          this.stack.push([row, col])
          return [row, col]
        }
      }
      return this.rollback()
    },
    insertValid(row, col, value){
      for (var r = 0; r < this.boardSize; r++){
        if (this.board[r][col] == value){
          return false
        }
      }
      for (var c = 0; c < this.boardSize; c++){
        if (this.board[row][c] == value){
          return false
        }
      }
      for (var r = row - (row % 3); r < (row + (3 - (row % 3))); r++){
        for (var c = col - (col % 3); c < (col + (3 - (col % 3))); c++){
          if (this.board[r][c] == value){
            return false
          }
        }
      }
      return true  
    },
    async solveBoard(){
      for(var r = 0; r < this.boardSize; r++){
        for(var c = 0; c < this.boardSize; c++){
          if (!this.board[r][c]){
            var inserted = false
            for (var i = 1; i <= this.boardSize; i++){
              if (this.insertValid(r ,c, i) && !inserted){
                Vue.set(this.board[r], c, i)
                this.stack.push([r,c])
                await this.sleep(100)
                inserted = true
                break
              }
            }
            if (!inserted){
              var retVal = this.rollback()
              r = retVal[0]
              c = retVal[1] - 1
            }
          }
        }
      }
      console.log('Done')
      // console.log(this.board)
    }
  },
  computed:{
    sudokuBoard(){
      return this.board;
    }
  },
  created(){
    this.board = []
    for(var r = 0; r < this.boardSize; r++){
      this.board.push([])
      for(var c = 0; c < this.boardSize; c++){
        this.board[r].push(0)
      }
    }
    // console.log(this.board)
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
li:nth-child(n):nth-child(-n+9) {
  border-top-width: 4px;
}
li:nth-child(n+73):nth-child(-n+81) {
  border-bottom-width: 4px;
}
li:nth-child(3n) {
  border-right-width: 4px;
}
li:nth-child(9n+1) {
  border-left-width: 4px;
}
li:nth-child(n+19):nth-child(-n+27) {
  border-bottom-width: 4px;
}
li:nth-child(n+46):nth-child(-n+54) {
  border-bottom-width: 4px;
}

ul {
  display: grid;
  grid-template-columns: repeat(9, 5vw);
  grid-template-rows: repeat(9, 5vw);
  justify-content: center;
  align-content: center;
  grid-gap: 0rem;
  list-style: none;
  margin: 0 0 2vw;
  padding: 0;
  font-size: calc(2vw + 10px);
}
li {
  margin: 0;
  padding: 0;
  text-align: center;
  border: 1px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  /* span {
    margin-top: 0.4rem;
  }   */
}

.note {
  background: #ddd;
  font-family: monospace;
  padding: 2em 5em;
  font-size: 120%;
  order: -1;
}
@supports (display:grid) {
  .note {display:none;}
}
</style>
