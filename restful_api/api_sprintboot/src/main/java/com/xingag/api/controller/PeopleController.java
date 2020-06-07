package com.xingag.api.controller;

import com.xingag.api.common.ApiResult;
import com.xingag.api.domain.People;
import com.xingag.api.service.PeopleService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/***
 * 对外暴露的接口
 * 欢迎关注公众号：AirPython
 */

@Api(value = "Restful API 服务")
@RestController
@RequestMapping("/v1")
public class PeopleController {

    @Autowired
    private PeopleService peopleService;

    /***
     * 所有记录
     * @return
     */
    @ApiOperation(value = "查询所有记录")
    @RequestMapping(value = "/all", method = RequestMethod.GET)
    public ApiResult getAllPeople() {
        List<People> peoples = peopleService.getAllPeoples();
        return ApiResult.success(peoples);
    }

    /***
     * 某一条记录
     * @param id
     * @return
     */
    @ApiOperation(value = "查询某一条记录")
    @RequestMapping(value = "/one/{id}", method = RequestMethod.GET)
    public ApiResult getOnePeople(@ApiParam(name = "id", value = "主键id", required = true) @PathVariable int id) {
        People people = peopleService.getOnePeople(id);
        if (null != people) {
            return ApiResult.success(people);
        } else {
            return ApiResult.failure("数据不存在");
        }
    }


    /***
     * 新增一条记录
     * {
     * 	"id":1,
     * 	"name":"1111",
     * 	"age":23,
     * 	"extra":true
     * }
     * @return
     */
    @ApiOperation(value = "新增某一条记录")
    @RequestMapping(value = "/add", method = RequestMethod.POST)
    public ApiResult updatePeople(@RequestBody People people) {
        boolean result = peopleService.addPeople(people);
        if (result) {
            return ApiResult.success("新增一条记录成功！");
        } else {
            return ApiResult.failure("新增失败！");
        }
    }


    /***
     * 更新一条记录
     * Body-form-data
     * id:27
     * name:星安果
     * age:18
     * extra:true
     * @param id
     * @param name
     * @param age
     * @param extra
     * @return
     */
    @ApiOperation(value = "更新某一条记录")
    @RequestMapping(value = "/update", method = RequestMethod.POST)
    public ApiResult updatePeople(@RequestParam int id, @RequestParam String name, @RequestParam int age, @RequestParam boolean extra) {
        People people = new People(id, name, age, extra);
        boolean result = peopleService.updatePeople(people);
        if (result) {
            return ApiResult.success("更新成功！");
        } else {
            return ApiResult.failure("更新失败！");
        }
    }

    /***
     * 删除一条记录
     * @param id  主键id
     * @return
     */
    @ApiOperation(value = "根据ID删除一条记录")
    @RequestMapping(value = "/delete", method = RequestMethod.DELETE)
    public ApiResult delFoo(@RequestParam int id) {
        Boolean result = peopleService.delPeople(id);
        if (result) {
            return ApiResult.success("删除成功！");
        } else {
            return ApiResult.failure("用户不存在，删除失败！");
        }
    }
}
