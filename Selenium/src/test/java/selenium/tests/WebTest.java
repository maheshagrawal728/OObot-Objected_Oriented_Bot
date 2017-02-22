package selenium.tests;

import static org.junit.Assert.*;

import java.util.List;
import java.util.concurrent.TimeUnit;
import selenium.fetch.allUseCases;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.ChromeDriverManager;

public class WebTest
{
	private static WebDriver driver;
	
	@BeforeClass
	public static void setUp() throws Exception 
	{
		//driver = new HtmlUnitDriver();
		ChromeDriverManager.getInstance().setup();
		driver = new ChromeDriver();
	}
	
	@AfterClass
	public static void  tearDown() throws Exception
	{
		driver.close();
		driver.quit();
	}


	@Test
	public void requestAvailablePattern() throws Exception
	{
		driver.get("https://seprojectbot.slack.com/");
		allUseCases testcase = new allUseCases();
		// Wait until page loads and we can see a sign in button.
		WebDriverWait wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement pw = driver.findElement(By.id("password"));

		// Type in our test user login info.
		email.sendKeys("mramali2@ncsu.edu");
		pw.sendKeys("****");

		// Click
		WebElement signin = driver.findElement(By.id("signin_btn"));
		signin.click();

		// Wait until we go to general channel.
		wait.until(ExpectedConditions.titleContains("general"));

		// Switch to #bots channel and wait for it to load.
		driver.get("https://seprojectbot.slack.com/messages/oobottesting");
		wait.until(ExpectedConditions.titleContains("oobottesting"));

		// Type something
		
		WebElement messageBot = driver.findElement(By.id("message-input"));
		String msg;
		List<WebElement> msgs;
		testcase.useCase1(driver,wait);
		testcase.useCase2(driver,wait);
		testcase.useCase3(driver,wait);
		/*
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
		
		// Use Case 2
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
		
		// Use Case 3
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
		*/
	}
}
