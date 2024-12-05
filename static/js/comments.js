document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");  // Get all edit buttons
    const commentText = document.getElementById("id_body");         // The textarea where comment is entered
    const commentForm = document.getElementById("commentForm");      // The form for comments
    const submitButton = document.getElementById("submitButton");    // The submit button for the form

    // Add click event listener to each edit button
    for (let button of editButtons) {
        button.addEventListener("click", function(e) {
            // Get the comment ID from the button's data-comment-id attribute
            const commentId = e.target.getAttribute("data-comment-id");
            // Get the content of the comment using the comment ID
            const commentContent = document.getElementById(`comment${commentId}`).innerText;

            // Populate the textarea with the comment content for editing
            commentText.value = commentContent;

            // Change the submit button's text to "Update"
            submitButton.innerText = "Update";

            // Change the form's action URL to the correct URL for editing this comment
            commentForm.setAttribute("action", `/edit_comment/${commentId}/`);  // The endpoint for editing the comment
        });
    }
});



/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}
