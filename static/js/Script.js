document.querySelectorAll('.card-wrapper').forEach(wrapper => {
    const card = wrapper.querySelector('.card');
    const glow = wrapper.querySelector('.card-glow');
    
    wrapper.addEventListener('mousemove', (e) => {
        const rect = wrapper.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = (y - centerY) / 25 * -1;
        const rotateY = (x - centerX) / 25;
        
        card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        
        glow.style.setProperty('--mouse-x', `${x}px`);
        glow.style.setProperty('--mouse-y', `${y}px`);
    });
    
    wrapper.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0) rotateY(0)';
    });
});

document.querySelectorAll("#myDuplicateId").disabled = true;

function Card(Name){
    document.getElementById(Name).disabled = false;
}