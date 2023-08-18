#rust/tokio

TODAY I LOOKED INTO TOKIO
[[Literature Notes/Rust/tokio]]
i read through the
https://tokio.rs/tokio/tutorial and did the first examples.

SUMMARY OF TOKIO:
`Tokio is an asynchronous runtime for the Rust programming language. It provides the building blocks needed for writing networking applications.`
(it can wait for functions that take longer times in a non blocking but halting way)

# When not to use Tokio
`Speeding up CPU-bound computations by running them in parallel on several threads. Tokio is designed for IO-bound applications where each individual task spends most of its time waiting for IO. If the only thing your application does is run computations in parallel, you should be using rayon`

[[11-Friday-August (23)#outline]]

I did got confused if asynchronous function are executed concurrently or synchronous.

After a confusing question round with chatgpt, I found out that async functions don't block the main thread but pause it, which means that you could run other tasks concurrently.

But just running 2 async function one after the other will execute them synchronously.

In order to add concurrency you have to spawn a tokio::task

```rust
#[tokio::main]
async fn main(){
tokio::task::spawn(move async {...some_async_function();});
}
```

Now if you would .await a async function, you could process the spawned task in the meantime while the main thread waits for the async function to end.

# ***ALL 3 EXAMPLES***

- Synchronous
```rust
use tokio::time::{Duration,sleep}
async fn wait3(){
sleep(Duration::from_secs(3)).await;
}

#[tokio::main]
async fn main(){
wait3.await;//starts and wait until done
wait3.await;//starts and wait until done
}
```
- Concurrent but interrupted by end of program
```rust
use tokio::time::{Duration,sleep}
async fn wait3(){
sleep(Duration::from_secs(3)).await;
}

async fn wait8(){
sleep(Duration::from_secs(8)).await;
}

#[tokio::main]
async fn main(){

//starts concurrent (waits 8 sek)
tokio::task::spawn(async move{wait8.await});

//starts while task is computing 
//(waits 3 sek)
wait3.await;

//task can't finish because program ends to fast
}
```

- Truly concurrent 
```rust
use tokio::time::{Duration,sleep}
async fn wait3(){
sleep(Duration::from_secs(3)).await;
}

async fn wait8(){
sleep(Duration::from_secs(8)).await;
}

#[tokio::main]
async fn main(){

//starts concurrent (waits 8 sek)
let join_handle=tokio::task::spawn
(async move{wait8.await});

//starts while task is computing 
//(waits 3 sek)
wait3.await;

//we also wait for the task to finish before ending the program
join_handle.await;
}
```

# outline
`Most computer programs are executed in the same order in which they are written. The first line executes, then the next, and so on. With synchronous programming, when a program encounters an operation that cannot be completed immediately, it will block until the operation completes. For example, establishing a TCP connection requires an exchange with a peer over the network, which can take a sizeable amount of time. During this time, the thread is blocked. With asynchronous programming, operations that cannot complete immediately are suspended to the background. The thread is not blocked, and can continue running other things. Once the operation completes, the task is unsuspended and continues processing from where it left off. Our example from before only has one task, so nothing happens while it is suspended, but asynchronous programs typically have many such tasks.`