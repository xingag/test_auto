package com.xingag.api;

import com.xingag.api.service.ScoreServiceImpl;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ScoreTests {

    private ScoreServiceImpl scoreService = new ScoreServiceImpl();

    private static final String[] RESULT_LEVEL = {"优秀","良好","合格","不合格","差","成绩格式不正确"};

    //成绩优秀
    @Test
    public void testLevelA() {
        Assert.assertEquals(RESULT_LEVEL[0], scoreService.getScoreLevel(95));
    }

    //成绩良好
    @Test
    public void testLevelB() {
        Assert.assertEquals(RESULT_LEVEL[1], scoreService.getScoreLevel(80));
    }

    //成绩及格
    @Test
    public void testLevelC() {
        Assert.assertEquals(RESULT_LEVEL[2], scoreService.getScoreLevel(70));
    }
}
