def inject_loader_script():
    return """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Apply base styles immediately
        document.body.style.backgroundColor = '#FFFFFF';
        
        // Create a style element for permanent rules
        const styleTag = document.createElement('style');
        styleTag.textContent = `
            [data-testid="stAppViewContainer"],
            [data-testid="stSidebar"],
            .stApp {
                background-color: #FFFFFF !important;
                color: #333 !important;
            }
        `;
        document.head.appendChild(styleTag);

        // MutationObserver for dynamic elements
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                mutation.addedNodes.forEach((node) => {
                    if (node.nodeType === 1) { // Element node
                        if (node.matches('[data-testid="stAppViewContainer"], [data-testid="stSidebar"], .stApp')) {
                            node.style.backgroundColor = '#FFFFFF';
                            node.style.color = '#333';
                        }
                        node.querySelectorAll?.('[data-testid="stAppViewContainer"], [data-testid="stSidebar"], .stApp').forEach(el => {
                            el.style.backgroundColor = '#FFFFFF';
                            el.style.color = '#333';
                        });
                    }
                });
            });
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
    </script>
    """