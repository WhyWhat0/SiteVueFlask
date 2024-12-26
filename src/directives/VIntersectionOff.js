export default {
    mounted(el, binding) {
        const options = {
          rootMargin: '0px',
          threshold: 1.0
        }
        const callback = (entries, observer) => {
          binding.value()
          if (!entries[0].isIntersecting) {
          }
        };
        const observer = new IntersectionObserver(callback, options);
        observer.observe(el);
    },
    name: 'intersection-off'
}
