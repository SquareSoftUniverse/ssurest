<template>
  <div class="chat-window">
    <div
      v-for="(post, index) in results"
      :key="index"
    >
      <span
        :style="{fontSize: `${post.handle.size}pt`, fontFamily: post.handle.font}"
      >
        <ChatHandle
          :color="post.handle.handle_color"
        >
          {{ post.handle.name }}
        </ChatHandle>
        <span class="handle-spacer">&nbsp;:&nbsp;</span>
        <ChatPost
          :color="post.handle.text_color"
        >
          {{ post.message }}
        </ChatPost>
      </span>
    </div>
  </div>
</template>

<script>
import chatPosts from "@/data/chatposts";
import ChatPost from "@/chat/ChatPost.vue";
import ChatHandle from "@/chat/ChatHandle.vue";

export default {
  name: "ChatWindow",
  components: {
    ChatPost,
    ChatHandle,
  },
  data() {
    const sortedResults = chatPosts.results.sort((a, b) =>
      a.datetime_posted > b.datetime_posted ? 1 : -1
    );
    chatPosts.results = sortedResults;
    return chatPosts;
  },
};
</script>

<style scoped>
.chat-window {
  width: 80%;
  justify-content: left;
}
.handle-spacer {
  color: #FFFFFF;
  font-weight: 100;
}
</style>
