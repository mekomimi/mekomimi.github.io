# Java开箱即用代码库

## 多线程

```java
package pers.studyForWorkExam.javaBase;

import java.util.concurrent.TimeUnit;

public class TestThread {
	public static void main(String[] args) {
		RunableClass r1= new RunableClass(1);
		RunableClass r2= new RunableClass(2);
		
		Thread t=new Thread(r1);
		Thread t2=new Thread(r2);
		
		ThreadClass threadClass=new ThreadClass();
        
		t.start();
		t2.start();
		threadClass.start();
	}
}

/*
 * 实现runable接口，再委托给Thread运行
 */
class RunableClass implements Runnable {
	
	int j;
	public RunableClass(int i) {
		this.j=i;
	}
	
	public void run() {
	    for (int i = 0; i < 10; i++) {
	    	System.out.println("hello Runable"+j);
	    	
	    	//暂停一秒看看效果
	    	try {
				TimeUnit.SECONDS.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}


/*
 * 继承Thread类，可直接调用实例的run方法
 */
class ThreadClass extends Thread{
	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			System.out.println("hello Thread");
			
			try {
				TimeUnit.SECONDS.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		super.run();
	}
}
```