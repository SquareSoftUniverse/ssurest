<template>
  <div class="chat-window">
    <div
      v-for="(post, index) in posts"
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
import ChatPost from "@/chat/ChatPost.vue";
import ChatHandle from "@/chat/ChatHandle.vue";
import axios from "axios";

export default {
  name: "ChatWindow",
  components: {
    ChatPost,
    ChatHandle,
  },
  data() {
    return {
      count: undefined,
      nextUrl: "",
      previousUrl: "",
      posts: [],
    }
  },
  async created() {
    await this.loadPosts();
  },
  methods: {
    async loadPosts() {
      const response = await axios.get("/api/posts");
      this.count = response.data.count;
      this.nextUrl = response.data.next;
      this.previousUrl = response.data.previous;
      this.posts = response.data.results;
    },
  }
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
