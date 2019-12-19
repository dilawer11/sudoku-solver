<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <SudokuSolver/>
  </div>
</template>

<script>
import SudokuSolver from './components/SudokuSolver'

export default {
  name: 'App',
  components: {
    SudokuSolver
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
