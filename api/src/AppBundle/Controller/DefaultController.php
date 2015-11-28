<?php

namespace AppBundle\Controller;

use FOS\RestBundle\Controller\FOSRestController;
use Symfony\Component\HttpFoundation\Request;
use FOS\RestBundle\Controller\Annotations as Rest;
use Symfony\Component\HttpFoundation\Response;

class DefaultController extends FOSRestController
{

    /**
     * @param Request $request
     * @Rest\Get("/get-burgers")
     *
     * @return Response
     */
    public function getBurgersAction(Request $request)
    {
        $view = $this->view([
            'status' => 'ok',
            'code' => 200
        ]);
        return $this->handleView($view);
    }

    /**
     * @param Request $request
     * @Rest\Put("/put-burger")
     *
     * @return Response
     */
    public function putBurgerAction(Request $request)
    {
        return $this->view([]);
    }
}
