<template>
  <div class="home">
    <ChatWindow />
    <br />
    <ChatBox />
  </div>
</template>

<script>
// @ is an alias to /src
import ChatWindow from "@/chat/ChatWindow.vue";
import ChatBox from "@/chat/ChatBox.vue";

export default {
  name: "Home",
  components: {
    ChatWindow,
    ChatBox,
  },
};
</script>
