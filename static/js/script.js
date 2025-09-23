// Script para interações do Old Dragon RPG
document.addEventListener('DOMContentLoaded', function() {
    // Efeitos sonoros e animações
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
        
        button.addEventListener('click', function() {
            // Efeito de clique
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Validação do formulário
    const form = document.querySelector('.character-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const name = document.getElementById('name').value.trim();
            if (!name) {
                e.preventDefault();
                alert('🎲 Por favor, digite um nome para seu personagem!');
                return;
            }
            
            const selectedRace = document.querySelector('input[name="race"]:checked');
            const selectedClass = document.querySelector('input[name="classe"]:checked');
            const selectedDistribution = document.querySelector('input[name="distribution"]:checked');
            
            if (!selectedRace || !selectedClass || !selectedDistribution) {
                e.preventDefault();
                alert('⚔️ Por favor, selecione todas as opções para criar seu personagem!');
                return;
            }
        });
    }

    // Efeitos visuais para as opções
    const options = document.querySelectorAll('.option-card');
    options.forEach(option => {
        option.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        option.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Rolagem de dados (para futuras implementações)
    window.rollDice = function(sides = 6) {
        return Math.floor(Math.random() * sides) + 1;
    };

    console.log('🐉 Old Dragon RPG - Sistema carregado!');
});