<template>
  <div class="chat-box">
    <input type="text" id="chat-input" class="chat-input" />
  </div>
</template>

<script>
export default {
  name: "ChatBox",
  data() {
    return {
      handle_id: 1,
      room_id: 1,
      post: "",
    };
  },
};
</script>

<style scoped>
.chat-box {
  align-content: center;
}
.chat-input {
  width: 50%;
  background-color: #333;
  color: #fff;
}
</style>
