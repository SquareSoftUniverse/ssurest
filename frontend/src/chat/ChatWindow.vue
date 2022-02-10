<template>
  <div class="chat-window">
    <div class="chat-post" v-for="(post, index) in results" :key="index">
      <ChatPost :post="post" />
    </div>
  </div>
</template>

<script>
import chatPosts from "@/data/chatposts";
import ChatPost from "@/chat/ChatPost.vue";
export default {
  name: "ChatWindow",
  components: {
    ChatPost,
  },
  data() {
    const sortedResults = chatPosts.results.sort(
      (a, b) =>
      a.datetime_posted > b.datetime_posted ? 1 : -1
    );
    chatPosts.results = sortedResults;
    return chatPosts;
  },
};
</script>

<style>
.chat-window {
  width: 80%;
  justify-content: left;
}
</style>
