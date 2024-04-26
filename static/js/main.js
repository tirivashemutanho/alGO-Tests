document.addEventListener("DOMContentLoaded", function() {
    // Get the form and form inputs
    var form = document.querySelector("form");
    var sortAlgorithmSelect = document.querySelector("select[name='sort_algorithm']");
    var sortBySelect = document.querySelector("select[name='sort_by']");
    var sortOrderSelect = document.querySelector("select[name='sort_order']");

    // Add event listeners to the form inputs
    sortAlgorithmSelect.addEventListener("change", submitForm);
    sortBySelect.addEventListener("change", submitForm);
    sortOrderSelect.addEventListener("change", submitForm);

    // Function to submit the form
    function submitForm() {
      var sortBy = sortBySelect.value;
      var sortOrder = sortOrderSelect.value;
  
      // Get the table body element
      var tableBody = document.querySelector("#student-table tbody");
  
      // Get all the rows in the table
      var rows = Array.from(tableBody.querySelectorAll("tr"));
  
      // Sort the rows based on the selected sort options
      rows.sort(function(a, b) {
          var valueA = a.querySelector("td:nth-child(" + (['firstname', 'lastname', 'date_of_birth', 'gender', 'contact_number', 'email', 'address', 'program', 'gpa', 'accommodation'].indexOf(sortBy) + 2) + ")").textContent.trim();
          var valueB = b.querySelector("td:nth-child(" + (['firstname', 'lastname', 'date_of_birth', 'gender', 'contact_number', 'email', 'address', 'program', 'gpa', 'accommodation'].indexOf(sortBy) + 2) + ")").textContent.trim();
  
          if (sortOrder === "ascending") {
              return valueA.localeCompare(valueB);
          } else {
              return valueB.localeCompare(valueA);
          }
      });
  
      // Remove existing rows from the table
      rows.forEach(function(row) {
          tableBody.removeChild(row);
      });
  
      // Append sorted rows back to the table
      rows.forEach(function(row) {
          tableBody.appendChild(row);
      });
  }
});