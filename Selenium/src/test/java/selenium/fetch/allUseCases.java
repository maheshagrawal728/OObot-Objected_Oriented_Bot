package selenium.fetch;

import static org.junit.Assert.assertTrue;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class allUseCases {

	
	public void useCase1(WebDriver driver, WebDriverWait wait) throws InterruptedException{
		WebElement messageBot = driver.findElement(By.id("message-input"));
		messageBot.sendKeys("@oobot can you get publish-subscribe pattern?");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		List<WebElement> msgs = driver.findElements(By.xpath("//text()[contains(.,'Do you want to download the files or want me to upload it to a repo?')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		String msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().contains("do you want to download the files or want me to upload it to a repo?"));
		Thread.sleep(3000);
		
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		messageBot.sendKeys("@oobot download");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);
		
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//msg = driver.findElement(By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[contains(.,'The template is available in the link: Here is the link to ur repo:')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("the template is available in the link: here is the link to ur repo:"));
		
		//requestUnavailablePattern
		messageBot.sendKeys("@oobot can you get factory pattern?");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);
		
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);

		msgs = driver.findElements(By.xpath("//text()[contains(.,'The pattern does not exist')]/ancestor::div//span[@class='message_body']"));
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		assertTrue(msg.toLowerCase().contains("the pattern does not exist"));
	}
	
	public void useCase2(WebDriver driver, WebDriverWait wait) throws InterruptedException{
		String msg;
		List<WebElement> msgs;
		WebElement messageBot = driver.findElement(By.id("message-input"));
		messageBot.sendKeys("@oobot can you store a template?");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[contains(.,'provide the pattern name and github link')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("provide the pattern name and github link"));
		
		messageBot.sendKeys("@oobot object pool4,https://github.com/rchand/singleton");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[starts-with(.,'Pattern added successfully')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().contains("pattern added successfully"));
		
		// Existing pattern
		messageBot.sendKeys("@oobot can you store a template?");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msgs = driver.findElements(By.xpath("//text()[contains(.,'provide the pattern name and github link')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("provide the pattern name and github link"));
		
		messageBot.sendKeys("@oobot publish-subscribe,https://github.com/rchand/publish-subscribe");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[starts-with(.,'The pattern already exists')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("the pattern already exists"));
		
	}
	public void useCase3(WebDriver driver, WebDriverWait wait) throws InterruptedException{
		String msg;
		List<WebElement> msgs;
		WebElement messageBot = driver.findElement(By.id("message-input"));
		messageBot.sendKeys("@oobot can you get the pattern from github ?");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[contains(.,'provide the pattern name to search for')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("provide the pattern name to search for"));
		
		messageBot.sendKeys("@oobot observor");
		messageBot.sendKeys(Keys.RETURN);
		Thread.sleep(3000);

		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		
		//String msg = driver.findElement(
			//	By.xpath("//span[@class='message_body']")).getText();
		msgs = driver.findElements(By.xpath("//text()[starts-with(.,'Here is what I thought might interest you...')]/ancestor::div//span[@class='message_body']"));
		//System.out.println(msgs.get(msgs.size()-1).getText());
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		msg = msgs.get(msgs.size()-1).getText();
		wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//System.out.println(msg);
		assertTrue(msg.toLowerCase().startsWith("here is what i thought might interest you..."));
	}
}
