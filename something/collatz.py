import streamlit as st

def collatz(a):
    if a<1:
        raise ValueError("Bro be positive") 
      
    path = [a]   
    steps=0  
    while(a!=1):
        if a%2==0:
            a=a//2
        else:
            a=3*a+1
        path.append(a)
        steps+=1
    return steps, path

def render():
    st.title("The Collatz Conjecture")
    st.markdown("just another conjecture...they say that it returns 1 whenever you let a positive number to flow past this!")

    n= st.number_input("Be positive and enter:", min_value=1, value=27, step=1)

    try:
       path = collatz(n)
       steps = len(path)-1
       peak = max(path)

       col1, col2 = st.columns(2)
       col1.metric("WTF are these numbers?", steps)
       col2.metric("How high?", peak)

       st.subheader("Holy path")
       st.line_chart(path, use_container_width=True)

    with st.expander("The whole Path"):
        st.write(join(map(str, path)))

except ValueError as e:
    st.error(str(e))


