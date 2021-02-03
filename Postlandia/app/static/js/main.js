
var app = new Vue({
  
  
  
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
      
      display_edit: "Edit",
      display_delete: "Delete",

      posts: [],
      new_post: '',
      user_wants_to_add_post: false,

      post_editable: false,

      new_post_edit: '',
      
  },
  
  methods: {
    
    get_posts: function() {

      var url = 'http://127.0.0.1:8000/api/post-list/'

      axios.get(url).then(result => {
        let current_posts = result.data

        this.posts = current_posts
      }).catch((error) => console.log("Some error : " + error))

      

    },

    add_post: function() {

      const csrftoken = Cookies.get('csrftoken');
      
      var create_url = 'http://127.0.0.1:8000/api/post-create/'

      axios({
        method: 'post',
        url : create_url,
        data: {text : this.new_post},
        headers:{
          'X-CSRFToken' : csrftoken    //Apparently in Django we need a CSRFtoken whenever we want to submit POST data. The way I get the token is by using a CDN : <script src="https://cdn.jsdelivr.net/npm/js-cookie@rc/dist/js.cookie.min.js"></script>. There are other ways to get it, shown in django documentation
        }
      }).then(result => {
        let post = result.data;
 
        this.posts = [post, ...this.posts];

        this.new_post = "";  //Resets the text field so that no previous string remains when a user wants to add another post

      }).catch(e => alert(e));

     

    },

    allow_new_post: function() {
      this.user_wants_to_add_post = true
    },

    unallow_new_post: function() {
      this.user_wants_to_add_post = false
    },

    clear_textarea_for_post: function(){
        this.new_post = ""
    },

    delete_post: function(post_id_to_be_deleted){

      var the_url = 'http://127.0.0.1:8000/api/post-delete/'

      the_url = the_url.concat(post_id_to_be_deleted)

      const csrftoken = Cookies.get('csrftoken');

      axios({
        method: 'delete',
        url : the_url,
        data: {pk : post_id_to_be_deleted},
        headers:{
          'X-CSRFToken' : csrftoken    //Apparently in Django we need a CSRFtoken whenever we want to submit data. The way I get the token is by using a CDN : <script src="https://cdn.jsdelivr.net/npm/js-cookie@rc/dist/js.cookie.min.js"></script>. There are other ways to get it, shown in django documentation
        }
      }).then(result => {

        this.posts = this.posts.filter((post) => post.id !== post_id_to_be_deleted);

      }).catch(e => alert(e));
      
    },

    

    
  },

   
  
})


app.get_posts()






