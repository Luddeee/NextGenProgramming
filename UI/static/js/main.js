document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('translationForm');
    const translateBtn = document.getElementById('translateBtn');
    const spinner = translateBtn.querySelector('.spinner-border');
    const resultDiv = document.getElementById('result');
    const codeOutput = document.getElementById('codeOutput');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        spinner.classList.remove('d-none');
        translateBtn.disabled = true;
        resultDiv.classList.add('d-none');

        try {
            const formData = new FormData(form);
            const response = await fetch('/translate', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            // Update code display
            codeOutput.textContent = data.code;
            //console.log('Execution Result:', data.result); //debugging code
            
            
            // Highlight code
            Prism.highlightElement(codeOutput);
            
            // Show results
            resultDiv.classList.remove('d-none');
        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            // Hide loading state
            spinner.classList.add('d-none');
            translateBtn.disabled = false;
        }
    });

    // Example problems functionality
    document.querySelectorAll('.example-problem').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('problem').value = this.textContent;
        });
    });
});
