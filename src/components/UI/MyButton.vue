<template>
    <button class="btn">
        <slot></slot>
    </button>
</template>
  
<script>
export default {
    name: 'my-button'
}
</script>
  
<style>
.btn {
    margin: 20px;
    padding: 5px;
    background: none;
    color: teal;
    border: 3px solid teal;
    border-radius: 7px;
    transition: 0.6s linear;
    font-size: large;
}

.btn:hover {
    background-color: aqua;
}
</style>
  