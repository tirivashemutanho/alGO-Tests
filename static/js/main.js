document.addEventListener('DOMContentLoaded', () => {
  // Get the sorting form
  const sortingForm = document.getElementById('sorting-form');
  const sortAlgorithm = document.getElementById('sort-algorithm');
  const sortBy = document.getElementById('sort-by');
  const sortOrder = document.getElementById('sort-order');

  // Add change event listener for form submission
  sortingForm.addEventListener('submit', submitForm);
  // sortAlgorithm.addEventListener('change', submitForm);
  sortBy.addEventListener('change', submitForm);
  sortOrder.addEventListener('change', submitForm);

  function submitForm(e) {
    e.preventDefault();
    const requestData = {
      algorithm: sortAlgorithm.value,
      sortBy: sortBy.value,
      sortOrder: sortOrder.value
    };
  
    fetch('/sort', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Request failed');
        }
      })
      .then(data => {
        updateTable(data);
      })
      .catch(error => {
        console.error('Request error:', error);
        // Handle the error here, e.g., display an error message to the user
      });
  }

function updateTable(data) {
  const tableBody = document.querySelector("#student-table tbody");

  // Clear existing rows from the table
  tableBody.innerHTML = '';
  num = 0
  // Append sorted rows back to the table
  data.forEach(student => {
    const row = document.createElement('tr');
    
    row.innerHTML = `
    <td>${ num ++ }</td>
    <td>${student.firstname}</td>
    <td>${student.lastname}</td>
    <td>${student.date_of_birth}</td>
    <td>${student.gender}</td>
    <td>${student.contact_number}</td>
    <td>${student.email}</td>
    <td>${student.address}</td>
    <td>${student.program}</td>
    <td>${student.gpa}</td>
    <td>${student.accommodation}</td>
    <td>
          <a href="uploads/${student.academic_transcripts_unique_filename}">${ student.academic_transcripts_unique_filename }</a>
    </td>
    <td>
          <a href="uploads/${student.personal_doc_unique_filename}">${ student.personal_doc_unique_filename }</a>
    </td>
    `;
    tableBody.appendChild(row);
  });
}
});