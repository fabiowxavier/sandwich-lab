const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const editButtons = document.getElementsByClassName("btn-edit[_{{{CITATION{{{_1{](https://github.com/cutlerwater/django_blog/tree/6c7e71f82af59e9bd28c5315428457d678d62aa5/App%2Fmodels.py)[_{{{CITATION{{{_2{](https://github.com/johntomnyone/Earn-Xtra-Cash-Blog/tree/c053dd5b176620ddd579f029e9a29b7992adfcde/blog%2Fmodels.py)[_{{{CITATION{{{_3{](https://github.com/hekl0/SimpleBlog/tree/6c0dcdf2e2a97eae87e56e623793f32eea50aed7/blog%2Fmodels.py)

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");  // Get comment ID
    let commentContent = document.getElementById(`comment${commentId}`).innerText;  // Get comment content
    commentText.value = commentContent;  // Set the textarea content to the comment's content
    submitButton.innerText = "Update";  // Change button text to "Update"
    
    // Update the form action to the correct edit URL for this comment
    commentForm.setAttribute("action", `/blog/${e.target.getAttribute("slug")}/edit_comment/${commentId}`);
  });
}

const deleteButtons = document.getElementsByClassName("btn-delete");

/**
* Initializes delete functionality for the provided delete buttons.
*
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Redirects the user to the delete URL for that comment.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");  // Ensure this is set correctly
    let slug = e.target.getAttribute("slug");  // Get the correct slug from the button

    // Ensure that both slug and commentId are valid before redirecting
    if (slug && commentId) {
      window.location.href = `/blog/${slug}/delete_comment/${commentId}/`; // Correct URL
    }
  });
}