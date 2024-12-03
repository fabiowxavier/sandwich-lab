const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.querySelector("button[type='submit']");

/*
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
    // Get the comment ID and content
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;

    // Fill the textarea with the comment content
    commentText.value = commentContent;

    // Change the submit button text to "Update"
    submitButton.innerText = "Update";

    // Update the form action URL to the edit URL
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