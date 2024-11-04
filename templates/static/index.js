const btnModal = document.getElementById('btnModal')


document.querySelectorAll('.cards').forEach(cards =>{
    cards.addEventListener('dragstart', e => {
        e.currentTarget.classList.add('opacity')
    })

    cards.addEventListener('dragend', e => {
        e.currentTarget.classList.remove('opacity')
    })
})

document.querySelectorAll('.kanban-card').forEach(card => {

    card.addEventListener('dragover', e => {
        e.preventDefault(); // Permite o drop
    });

    card.addEventListener('drop', e => {
        
        const dragCard = document.querySelector('.cards.opacity');
        const tarefaId = dragCard.querySelector('#idTarefa')
        const statusTarefas = card.getAttribute('data-id'); 
        let status = 'A' 
        if (statusTarefas == '1'){
            status = 'N'
        } else if (statusTarefas == '2'){
            status = 'A'
        } else {
            status = 'C'
        }
 
        fetch(`/atualizar-status/${tarefaId.textContent}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ status: status })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                card.appendChild(dragCard);
            } else {
                console.error('Erro ao atualizar status da tarefa:', data.message);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });

})



document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal');
    const btnModal = document.getElementById('btnModal');
    const closeModalButton = document.getElementById('closeModalButton');

    // Adicionar ouvinte para abrir o modal
    btnModal.addEventListener('click', (e) => {
        console.log('clicou');
        modal.classList.remove('hidden');
    });



    closeModalButton.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}