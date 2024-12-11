document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModalElement = document.getElementById("deleteModal");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    if (!deleteModalElement) {
        console.error('deleteModalElement is not defined');
        return;
    }

    

    // Add click event listener to each edit button
    for (let button of editButtons) {
        button.addEventListener("click", function(e) {
            const commentId = e.target.getAttribute("data-comment-id");
            const commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `/edit_comment/${commentId}/`);
        });
    }

    // Add click event listener to each delete button
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            
        });
    }
});